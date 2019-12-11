import traceback
from flask_restful import Resource
from flask import request
import re

from datetime import datetime, timedelta

from libs import chatbot_helper, log_linechatbot as logs, \
    sale_accum_month, beacon_helper, \
    menu_01_sale_timeline as m1_SDH, \
    leadlag_bg_all, leadlag_bg_project, \
    menu_02_01_ll_sdh_subbg, menu_02_01_ll_sdh_period, \
    menu_01_01_ll_allbg_period, menu_01_01_ll_allbg_period_show_Q, \
    menu_01_01_ll_allbg_period_show_M, menu_01_01_ll_allbg_period_show_W, \
    menu_01_01_ll_allbg_period_show_Y, menu_01_01_ll_allbg_period_show_A, \
    menu_05_ap_phonebook, menu_04_01_actual_income_show_y2d, menu_executive_report, \
    menu_01_01_ll_allbg_sel_bg, menu_01_01_ll_allbg_period_show_L_C, \
    menu_02_01_ll_allbg_sel_subbg, menu_02_01_ll_allbg_subbg_period, \
    menu_02_01_ll_allbg_subbg_period_show, menu_02_01_ll_allbg_subbg_period_show_L_C, \
    menu_03_01_ll_allbg_byproject_period_show, menu_03_01_ll_allbg_byproject_period_show_L_C, \
    menu_04_01_actual_income_period, menu_04_01_actual_income_show_daily, \
    chatbot_register

from config import CHANNEL_ACCESS_TOKEN, REPLY_WORDING, \
    REPLY_SALCE_ACCM_B_M_WORDING, REPLY_SALCE_ACCM_C_M_WORDING, \
    DEFAULT_REPLY_WORDING, \
    MENU_01_VIP, MENU_01_VIP_BG, \
    LL_MSG_All, LL_MSG_PROJ, MENU_02_VIP, \
    LL_MSG_SUB_PERIOD, LL_MSG_ALLBG_PERIOD, \
    LL_MSG_APPHONEBOOK, LL_MSG_APPHONEBOOK2, \
    AC_ACTUAL_INCOME, EXECUTIVE_REPORT, \
    MENU_02_VIP_BG, LL_MSG_ALLSUBBG_PERIOD, LL_MSG_AC_Y2D, \
    LL_MSG_AC_DAILY, REGISTER_MSG


from models.chatbot_mst_user import MstUserModel
from models.log_linechatbot import LogChatBotModel
from models.crm_line_actual_income import ActualIncomeModel
from models.crm_line_ll_data import LeadLagModel
from models.crm_line_exct_report import ExecutiveReportModel
from models.vw_crm_line_actual_income import ActualIncomeByProjModel


class ChatBot(Resource):
    @classmethod
    def get(cls):
        return {"message": "Hello World"}, 200


class ChatBotRegister(Resource):
    @classmethod
    def post(cls):
        payload = request.get_json()
        print(payload)

        reply_token = payload['events'][0]['replyToken']
        source_type = payload['events'][0]['source']['type']
        timestamps = payload['events'][0]['timestamp']

        # get event type beacon or message
        events_type = payload['events'][0]['type']
        # print(events_type)

        groupId = None
        userId = None
        stickerId = None
        packageId = None
        msg_text = None
        name = None
        beacon_hwid = None
        beacon_dm = None
        beacon_type = None

        # Register Flag
        register_flag = 'N'

        try:
            groupId = payload['events'][0]['source']['groupId']
            userId = payload['events'][0]['source']['userId']
            # print(userId, groupId)
        except:
            userId = payload['events'][0]['source']['userId']

        if events_type == 'message':
            msg_type = payload['events'][0]['message']['type']
        elif events_type == 'postback':
            msg_type = 'postback'
        else:
            msg_type = 'beacon'

        reply_msg = None

        if msg_type == 'text':
            msg_text = payload['events'][0]['message']['text']
            message = msg_text
            # print(userId)
            user = MstUserModel().check_auth_by_token_id(userId)

            if user:
                # print("found")
                if message == MENU_01_VIP:  # LL ALL BG
                    vip = MstUserModel().check_VIP_auth_by_token_id(userId)
                    if vip:
                        # menu_01_01_ll_allbg_period.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                        menu_01_01_ll_allbg_sel_bg.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                    else:
                        reply_msg = "You are not authorized to access this menu."
                        chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                elif re.match(MENU_01_VIP_BG, message):  # Select BG
                    # LL[0] BY[1] BG[2] <1-4>[3]
                    bg = message.split(' ')[3]
                    menu_01_01_ll_allbg_period.replyMsg(reply_token, bg, CHANNEL_ACCESS_TOKEN)
                # elif message in MENU_01_01_SDH:
                #     m1_SDH.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                # Lead Lag
                elif message in LL_MSG_All:
                    leadlag_bg_all.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                elif message in MENU_02_VIP:  # menu_02_01_ll_allbg_subbg
                    menu_02_01_ll_allbg_sel_subbg.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                elif re.match(MENU_02_VIP_BG, message):  # Select Sub BG
                    # LL[0] BY[1] SubBG[2] <1-4>[1.0][3]
                    value = message.split(' ')[3]
                    bg = value.split('[')[0]
                    subbg = value.split('[')[1][:-1]
                    menu_02_01_ll_allbg_subbg_period.replyMsg(reply_token, bg, subbg, CHANNEL_ACCESS_TOKEN)
                elif re.match(LL_MSG_ALLSUBBG_PERIOD, message):  # LL BY BG Period
                    p_period = message.replace(LL_MSG_ALLSUBBG_PERIOD, "").strip()
                    val = re.match(r"[^[]*\[([^]]*)\]", p_period).groups()[0]
                    bg = val.split('-')[0].strip()
                    subbg = val.split('-')[1].strip()
                    period = None
                    if p_period[0] == 'Q':  # Quarter
                        period = 'QTD'
                    elif p_period[0] == 'W':  # Week
                        period = 'W'
                    elif p_period[0] == 'A':  # As of Current
                        period = 'YTD'

                    if p_period[0] != 'W':
                        ll_model = LeadLagModel().find_by_subbg_period('SUBBG', bg, subbg, period, 'Y')
                        menu_02_01_ll_allbg_subbg_period_show.replyMsg(reply_token, bg, subbg, ll_model,
                                                                       CHANNEL_ACCESS_TOKEN)
                    else:
                        ll_model_current = LeadLagModel().find_by_subbg_period('SUBBG', bg, subbg, period, 'Y')
                        ll_model_last_week = LeadLagModel().find_by_subbg_period('SUBBG', bg, subbg, period, 'N')
                        menu_02_01_ll_allbg_subbg_period_show_L_C.replyMsg(reply_token, bg, subbg,
                                                                           ll_model_current,
                                                                           ll_model_last_week,
                                                                           CHANNEL_ACCESS_TOKEN)
                elif re.match(LL_MSG_PROJ, message):  # proj:
                    value = message.split(',')
                    project = value[0].split(':')[1].strip()
                    p_period = value[1].split(':')[1].strip()

                    period = None
                    if p_period[0] == 'Q':  # Quarter
                        period = 'QTD'
                    elif p_period[0] == 'W':  # Week
                        period = 'W'
                    elif p_period[0] == 'Y':  # Year to Date
                        period = 'YTD'

                    if p_period[0] != 'W':
                        # ll_model = LeadLagModel().find_by_subbg_period('SUBBG', bg, subbg, period, 'Y')
                        ll_model = LeadLagModel().find_by_project_period('PROJ', project, period, 'Y')
                        menu_03_01_ll_allbg_byproject_period_show.replyMsg(reply_token, ll_model, CHANNEL_ACCESS_TOKEN)
                    else:
                        ll_model_current = LeadLagModel().find_by_project_period('PROJ', project, period, 'Y')
                        ll_model_last_week = LeadLagModel().find_by_project_period('PROJ', project, period, 'N')
                        menu_03_01_ll_allbg_byproject_period_show_L_C.replyMsg(reply_token, ll_model_current,
                                                                               ll_model_last_week,
                                                                               CHANNEL_ACCESS_TOKEN)
                # Period Select ALL BG
                elif re.match(LL_MSG_ALLBG_PERIOD, message):  # LL BY BG Period
                    peroid = message.replace(LL_MSG_ALLBG_PERIOD, "").strip()
                    bg = re.match(r"[^[]*\[([^]]*)\]", peroid).groups()[0]
                    if peroid[0] == 'Q':  # Quarter
                        period = 'QTD'
                    # elif peroid[0] == 'M':  # Month
                    #     period = 'M'
                    elif peroid[0] == 'W':  # Week
                        period = 'W'
                    # elif peroid[0] == 'Y':  # Yesterday
                    #     period = 'Y'
                    elif peroid[0] == 'A':  # As of Current
                        period = 'YTD'

                    if period[0] != 'W':
                        ll_model = LeadLagModel().find_by_bg_period('BG', bg, period, 'Y')
                        menu_01_01_ll_allbg_period_show_W.replyMsg(reply_token, bg, ll_model, CHANNEL_ACCESS_TOKEN)
                    else:
                        ll_model_current = LeadLagModel().find_by_bg_period('BG', bg, period, 'Y')
                        ll_model_last_week = LeadLagModel().find_by_bg_period('BG', bg, period, 'N')
                        menu_01_01_ll_allbg_period_show_L_C.replyMsg(reply_token, bg,
                                                                     ll_model_current,
                                                                     ll_model_last_week,
                                                                     CHANNEL_ACCESS_TOKEN)

                # Period Select by Sub BG
                elif re.match(LL_MSG_SUB_PERIOD, message):
                    menu_02_01_ll_sdh_period.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                # # AP PhoneBook Menu 5
                # elif (re.match(LL_MSG_APPHONEBOOK, message)) or (re.match(LL_MSG_APPHONEBOOK2, message)):
                #     menu_05_ap_phonebook.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                # elif message in REPLY_SALCE_ACCM_B_M_WORDING:
                #     sale_accum_month.replyMsg(reply_token, reply_msg, "-1", CHANNEL_ACCESS_TOKEN)
                # elif message in REPLY_SALCE_ACCM_C_M_WORDING:
                #     sale_accum_month.replyMsg(reply_token, reply_msg, "0", CHANNEL_ACCESS_TOKEN)
                elif message in AC_ACTUAL_INCOME:  # Actual income select period
                    actual_income = ActualIncomeModel().find_all()
                    # menu_04_01_actual_income_show_y2d.replyMsg(reply_token, actual_income, CHANNEL_ACCESS_TOKEN)
                    menu_04_01_actual_income_period.replyMsg(reply_token, CHANNEL_ACCESS_TOKEN)
                elif re.match(LL_MSG_AC_Y2D, message):  # Actual income select Year to Date
                    actual_income = ActualIncomeModel().find_all()
                    menu_04_01_actual_income_show_y2d.replyMsg(reply_token, actual_income, CHANNEL_ACCESS_TOKEN)
                elif re.match(LL_MSG_AC_DAILY, message):  # Actual income select Daily by Project
                    yesterday = datetime.now() - timedelta(days=1)

                    values = ActualIncomeByProjModel().find_by_date(datetime.now().strftime('%Y%m%d'))
                    last_values = ActualIncomeByProjModel().find_by_date(yesterday.strftime('%Y%m%d'))

                    menu_04_01_actual_income_show_daily.replyMsg(reply_token, None,
                                                                 values,
                                                                 last_values,
                                                                 datetime.now().strftime('%d/%m/%Y'),
                                                                 yesterday.strftime('%d/%m/%Y'),
                                                                 CHANNEL_ACCESS_TOKEN)
                elif message in EXECUTIVE_REPORT:
                    executive_model = ExecutiveReportModel().find_by_id()
                    menu_executive_report.replyMsg(reply_token, executive_model, CHANNEL_ACCESS_TOKEN)
                elif message in REPLY_WORDING:
                    reply_msg = DEFAULT_REPLY_WORDING
                    # Reply Message Default Post API
                    chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
            else:
                # print("not found")
                if re.match(REGISTER_MSG, message):
                    register_flag = 'Y'

                    reply_msg = "We have received your registration. Please wait for confirmation within 10 minutes."
                    chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                    # chatbot_register.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                    # print("Register Msg")
                else:
                    # reply_msg = "You are not authorized to access this menu. please register from link line://app/1653377835-peowRY0O"
                    # chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                    if not groupId:
                        chatbot_register.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
        elif msg_type == 'postback':
            param_data = payload['events'][0]['postback']['data']
            param_date = payload['events'][0]['postback']['params']['date']
            date_val = param_date.replace("-", "").strip()
            # print(param_data, date_val)
            if re.match(LL_MSG_AC_DAILY, param_data):  # Actual income select Daily by Project
                values = ActualIncomeByProjModel().find_by_date(date_val)
                menu_04_01_actual_income_show_daily.replyMsg(reply_token, None,
                                                             values,
                                                             param_date,
                                                             CHANNEL_ACCESS_TOKEN)
        elif msg_type == 'beacon':
            beacon_hwid = payload['events'][0]['beacon']['hwid']
            beacon_dm = payload['events'][0]['beacon']['dm']
            beacon_type = payload['events'][0]['beacon']['type']
            stickerId = None
            packageId = None
            msg_text = None

            user = MstUserModel().find_by_token_id(userId)

            if user:
                log = LogChatBotModel().find_by_token_beacon_today(userId)

                # Check Revisit..!!
                # if log:
                #     msg_text = "Hello World Beacon K.{} Revisit..!!".format(user.user_full_name)
                # else:
                #     msg_text = "Hello World Beacon K.{} New Walk..".format(user.user_full_name)
                if not log:
                    msg_text = "Hello World Beacon K.{} New Walk..".format(user.user_full_name)

                beacon_helper.replyMsg(reply_token, msg_text, CHANNEL_ACCESS_TOKEN)
        else:
            if msg_type == 'sticker':
                stickerId = payload['events'][0]['message']['stickerId']
                packageId = payload['events'][0]['message']['packageId']
            else:
                stickerId = None
                packageId = None
                msg_text = None

        # Save Log to DB
        logs.savechatlog2db(reply_token, groupId,
                            userId, source_type,
                            timestamps, msg_type,
                            msg_text, stickerId, packageId,
                            beacon_hwid, beacon_dm, beacon_type,
                            register_flag)

        return {"message": "Register Line Push and Reply Message Successful"}, 201
