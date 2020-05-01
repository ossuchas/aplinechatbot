import traceback
from flask_restful import Resource
from flask import request
import re

from datetime import datetime, timedelta

from libs import chatbot_helper, log_linechatbot as logs, \
    beacon_helper, \
    leadlag_bg_all, menu_02_01_ll_sdh_period, \
    menu_01_01_ll_allbg_period, \
    menu_01_01_ll_allbg_period_show_W, \
    menu_04_01_actual_income_show_y2d, \
    menu_01_01_ll_allbg_sel_bg, menu_01_01_ll_allbg_period_show_L_C, \
    menu_02_01_ll_allbg_sel_subbg, menu_02_01_ll_allbg_subbg_period, \
    menu_02_01_ll_allbg_subbg_period_show, menu_02_01_ll_allbg_subbg_period_show_L_C, \
    menu_03_01_ll_allbg_byproject_period_show, menu_03_01_ll_allbg_byproject_period_show_L_C, \
    menu_04_01_actual_income_period, menu_04_01_actual_income_show_daily, \
    chatbot_register, menu_demo_app, menu_05_01_ex_rpt_period, \
    menu_05_01_ex_rpt_show_year_quarter, menu_05_01_ex_rpt_show_week, \
    menu_04_01_acgrs_income_show_y2d, chatbot_rich_menu, share_location, \
    menu_06_01_pm_value, check_pm_airvisual, virus_corona_stat, \
    menu_06_01_hotissue, menu_05_01_ex_rpt_show_year2date, \
    menu_07_01_dashboard

from config import CHANNEL_ACCESS_TOKEN, REPLY_WORDING, \
    DEFAULT_REPLY_WORDING, \
    MENU_01_VIP, MENU_01_VIP_BG, \
    LL_MSG_All, LL_MSG_PROJ, MENU_02_VIP, \
    LL_MSG_SUB_PERIOD, LL_MSG_ALLBG_PERIOD, \
    AC_ACTUAL_INCOME, EXECUTIVE_REPORT, \
    MENU_02_VIP_BG, LL_MSG_ALLSUBBG_PERIOD, LL_MSG_AC_Y2D, \
    LL_MSG_AC_DAILY, REGISTER_MSG, DEMO_APP, REGISTER_REJECT_MSG, \
    EXECUTIVE_PREFIX, BOOKING_INCOME, DASHBOARD_CARD, \
    RICH_MENU_MAIN, RICH_MENU_SECOND, \
    CHECK_PM, VIRUS, HOT_ISSUE, \
    RICH_MENU_MAIN_IT, RICH_MENU_MAIN_LCM, RICH_MENU_MAIN_MKT, \
    RICH_MENU_MAIN_SUBBG, RICH_MENU_MAIN_VIP, RICH_MENU_MAIN_VIP2, \
    RICH_MENU_SECOND_IT, RICH_MENU_SECOND_LCM, RICH_MENU_SECOND_MKT, \
    RICH_MENU_SECOND_SUBBG, RICH_MENU_SECOND_VIP, RICH_MENU_SECOND_VIP2


from models.chatbot_mst_user import MstUserModel
from models.log_linechatbot import LogChatBotModel
from models.crm_line_actual_income import ActualIncomeModel
from models.crm_line_ll_data import LeadLagModel
from models.crm_line_exct_report import ExecutiveReportModel
from models.vw_crm_line_actual_income import ActualIncomeByProjModel
from models.crm_line_gross_income import GrossIncomeModel
from models.vw_crm_line_userroleproj import UserRoleProjModel
from models.tmp_virus_corona import VirusCoronaModel


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
        register_empid = None
        register_email = None

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
                    menu_01_01_ll_allbg_sel_bg.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                    # Modified by Suchat S. 2020-01-09 for all access this menu
                    # # vip = MstUserModel().check_VIP_auth_by_token_id(userId)
                    # vip = MstUserModel().check_clevel_auth_by_token_id(userId)
                    # if vip:
                    #     # menu_01_01_ll_allbg_period.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                    #     menu_01_01_ll_allbg_sel_bg.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                    # else:
                    #     reply_msg = "You are not authorized to access this menu."
                    #     chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
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
                    vip2 = MstUserModel().check_VIP2_auth_by_token_id(userId)

                    if vip2:
                        reply_msg = "You are not authorized to access this menu."
                        chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                    else:
                        menu_02_01_ll_allbg_sel_subbg.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                elif re.match(MENU_02_VIP_BG, message):  # Select Sub BG
                    # LL[0] BY[1] SubBG[2] <1-4>[1.0][3]
                    value = message.split(' ')[3]
                    bg = value.split('[')[0]
                    subbg = value.split('[')[1][:-1]
                    prefix_bg = value.split('[')[1][:-3].strip()

                    vip = MstUserModel().check_VIP_auth_by_token_id(userId)
                    if vip:
                        menu_02_01_ll_allbg_subbg_period.replyMsg(reply_token, bg, subbg, CHANNEL_ACCESS_TOKEN)
                    else:
                        userModel = MstUserModel().find_by_token_id(_user_token_id=userId)

                        if userModel.user_type == 'SUBBG':
                            if userModel.user_sub_no[0].strip() == prefix_bg:  # Check authorized by bg
                                menu_02_01_ll_allbg_subbg_period.replyMsg(reply_token, bg, subbg, CHANNEL_ACCESS_TOKEN)
                            else:
                                reply_msg = "You are not authorized to access this menu."
                                chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                        elif userModel.user_type == 'MKT':  # Modified by Suchat S. 2020-01-29 for add MKT Role
                            if userModel.user_sub_no.strip() == subbg:  # Check authorized by bg
                                menu_02_01_ll_allbg_subbg_period.replyMsg(reply_token, bg, subbg, CHANNEL_ACCESS_TOKEN)
                            else:
                                reply_msg = "You are not authorized to access this menu."
                                chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                        elif userModel.user_type == 'LCM':
                            if userModel.user_sub_no.strip() == subbg:
                                menu_02_01_ll_allbg_subbg_period.replyMsg(reply_token, bg, subbg, CHANNEL_ACCESS_TOKEN)
                            else:
                                reply_msg = "You are not authorized to access this menu."
                                chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
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
                    # print(f"{value}, {project}, {p_period}")

                    period = None
                    if p_period[0] == 'Q':  # Quarter
                        period = 'QTD'
                    elif p_period[0] == 'W':  # Week
                        period = 'W'
                    elif p_period[0] == 'Y':  # Year to Date
                        period = 'YTD'

                    vip = MstUserModel().check_VIP_auth_by_token_id(userId)
                    if vip:
                        if p_period[0] != 'W':
                            # ll_model = LeadLagModel().find_by_subbg_period('SUBBG', bg, subbg, period, 'Y')
                            ll_model = LeadLagModel().find_by_project_period('PROJ', project, period, 'Y')
                            menu_03_01_ll_allbg_byproject_period_show.replyMsg(reply_token, ll_model,
                                                                               CHANNEL_ACCESS_TOKEN)
                        else:
                            ll_model_current = LeadLagModel().find_by_project_period('PROJ', project, period, 'Y')
                            ll_model_last_week = LeadLagModel().find_by_project_period('PROJ', project, period, 'N')
                            menu_03_01_ll_allbg_byproject_period_show_L_C.replyMsg(reply_token, ll_model_current,
                                                                                   ll_model_last_week,
                                                                                   CHANNEL_ACCESS_TOKEN)
                    else:  # for SubBG and LCM
                        userModel = MstUserModel().find_by_token_id(userId)

                        if userModel.user_type == 'SUBBG':
                            bg = userModel.user_sub_no[0].strip()
                            role = UserRoleProjModel().check_auth_subbg(userId, project, bg)
                            if role:
                                if p_period[0] != 'W':
                                    # ll_model = LeadLagModel().find_by_subbg_period('SUBBG', bg, subbg, period, 'Y')
                                    ll_model = LeadLagModel().find_by_project_period('PROJ', project, period, 'Y')
                                    menu_03_01_ll_allbg_byproject_period_show.replyMsg(reply_token, ll_model,
                                                                                       CHANNEL_ACCESS_TOKEN)
                                else:
                                    ll_model_current = LeadLagModel().find_by_project_period('PROJ', project, period,
                                                                                             'Y')
                                    ll_model_last_week = LeadLagModel().find_by_project_period('PROJ', project, period,
                                                                                               'N')
                                    menu_03_01_ll_allbg_byproject_period_show_L_C.replyMsg(reply_token,
                                                                                           ll_model_current,
                                                                                           ll_model_last_week,
                                                                                           CHANNEL_ACCESS_TOKEN)
                            else:
                                reply_msg = "You are not authorized to access this menu."
                                chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                        elif userModel.user_type == 'MKT':  # Modified by Suchat S. 2020-01-29 add MKT Role
                            subbg = userModel.user_sub_no.strip()
                            role = UserRoleProjModel().check_auth_lcm(userId, project, subbg)
                            if role:
                                if p_period[0] != 'W':
                                    ll_model = LeadLagModel().find_by_project_period('PROJ', project, period, 'Y')
                                    menu_03_01_ll_allbg_byproject_period_show.replyMsg(reply_token, ll_model,
                                                                                       CHANNEL_ACCESS_TOKEN)
                                else:
                                    ll_model_current = LeadLagModel().find_by_project_period('PROJ', project, period,
                                                                                             'Y')
                                    ll_model_last_week = LeadLagModel().find_by_project_period('PROJ', project, period,
                                                                                               'N')
                                    menu_03_01_ll_allbg_byproject_period_show_L_C.replyMsg(reply_token,
                                                                                           ll_model_current,
                                                                                           ll_model_last_week,
                                                                                           CHANNEL_ACCESS_TOKEN)
                            else:
                                reply_msg = "You are not authorized to access this menu."
                                chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                        elif userModel.user_type == 'LCM':
                            subbg = userModel.user_sub_no.strip()
                            role = UserRoleProjModel().check_auth_lcm(userId, project, subbg)
                            # print(role)
                            if role:
                                if p_period[0] != 'W':
                                    # ll_model = LeadLagModel().find_by_subbg_period('SUBBG', bg, subbg, period, 'Y')
                                    ll_model = LeadLagModel().find_by_project_period('PROJ', project, period, 'Y')
                                    menu_03_01_ll_allbg_byproject_period_show.replyMsg(reply_token, ll_model,
                                                                                       CHANNEL_ACCESS_TOKEN)
                                else:
                                    ll_model_current = LeadLagModel().find_by_project_period('PROJ', project, period,
                                                                                             'Y')
                                    ll_model_last_week = LeadLagModel().find_by_project_period('PROJ', project, period,
                                                                                               'N')
                                    menu_03_01_ll_allbg_byproject_period_show_L_C.replyMsg(reply_token,
                                                                                           ll_model_current,
                                                                                           ll_model_last_week,
                                                                                           CHANNEL_ACCESS_TOKEN)
                            else:
                                reply_msg = "You are not authorized to access this menu."
                                chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                        else:
                            reply_msg = "You are not authorized to access this menu."
                            chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                # Period Select ALL BG
                elif re.match(LL_MSG_ALLBG_PERIOD, message):  # LL BY BG Period
                    peroid = message.replace(LL_MSG_ALLBG_PERIOD, "").strip()
                    bg = re.match(r"[^[]*\[([^]]*)\]", peroid).groups()[0]
                    period = None
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
                elif message in AC_ACTUAL_INCOME:  # Actual income select period
                    # actual_income = ActualIncomeModel().find_all()
                    # menu_04_01_actual_income_show_y2d.replyMsg(reply_token, actual_income, CHANNEL_ACCESS_TOKEN)

                    # vip = MstUserModel().check_VIP_auth_by_token_id(userId)
                    vip = MstUserModel().check_clevel_auth_by_token_id(userId)
                    if vip:
                        menu_04_01_actual_income_period.replyMsg(reply_token, CHANNEL_ACCESS_TOKEN)
                    else:
                        reply_msg = "You are not authorized to access this menu."
                        chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                elif re.match(LL_MSG_AC_Y2D, message):  # Actual income select Year to Date
                    actual_income = ActualIncomeModel().find_all()
                    menu_04_01_actual_income_show_y2d.replyMsg(reply_token, actual_income, CHANNEL_ACCESS_TOKEN)
                elif re.match(LL_MSG_AC_DAILY, message):  # Actual income select Daily by Project
                    yesterday = datetime.now() - timedelta(days=1)
                    # print(type(yesterday))
                    before_yesterday = datetime.now() - timedelta(days=2)

                    values = ActualIncomeByProjModel().find_by_date(datetime.now().strftime('%Y%m%d'))

                    p_yesterday = ActualIncomeByProjModel().get_previousday("1")[0]
                    # print(p_yesterday)
                    last_values = ActualIncomeByProjModel().find_by_date(p_yesterday.strftime('%Y%m%d'))
                    # last_values = ActualIncomeByProjModel().find_by_date(yesterday.strftime('%Y%m%d'))
                    # before_last_values = ActualIncomeByProjModel().find_by_date(before_yesterday.strftime('%Y%m%d'))
                    p_before_yesterday = ActualIncomeByProjModel().get_previousday("2")[0]
                    # print(p_before_yesterday)
                    before_last_values = ActualIncomeByProjModel().find_by_date(p_before_yesterday.strftime("%Y%m%d"))

                    menu_04_01_actual_income_show_daily.replyMsg(reply_token, None,
                                                                 values,
                                                                 last_values,
                                                                 before_last_values,
                                                                 datetime.now().strftime('%d/%m/%Y'),
                                                                 p_yesterday.strftime('%d/%m/%Y'),
                                                                 p_before_yesterday.strftime('%d/%m/%Y'),
                                                                 CHANNEL_ACCESS_TOKEN)
                elif message in EXECUTIVE_REPORT:
                    # vip = MstUserModel().check_VIP_auth_by_token_id(userId)
                    vip = MstUserModel().check_clevel_auth_by_token_id(userId)
                    if vip:
                        menu_05_01_ex_rpt_period.replyMsg(reply_token, CHANNEL_ACCESS_TOKEN)
                    else:
                        reply_msg = "You are not authorized to access this menu."
                        chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                elif re.match(BOOKING_INCOME, message):
                    # print(message)
                    grs_model = GrossIncomeModel().find_all()
                    menu_04_01_acgrs_income_show_y2d.replyMsg(reply_token, grs_model, CHANNEL_ACCESS_TOKEN)
                elif re.match(EXECUTIVE_PREFIX, message):  # Executive by period
                    period = message.replace(EXECUTIVE_PREFIX, "").strip()
                    p_period = None
                    if period[0] != 'W':
                        if period[0] == 'A':
                            p_period = 'YTD'
                            ex_model = ExecutiveReportModel().find_by_period(p_period)
                            # print(f"kai AAA {p_period}")
                            menu_05_01_ex_rpt_show_year2date.replyMsg(reply_token, ex_model, CHANNEL_ACCESS_TOKEN)
                        else:
                            p_period = 'QTD'
                            ex_model = ExecutiveReportModel().find_by_period(p_period)
                            # print(f"kai BBB {p_period}")
                            menu_05_01_ex_rpt_show_year_quarter.replyMsg(reply_token, ex_model, CHANNEL_ACCESS_TOKEN)
                    else:
                        curr_ex_model = ExecutiveReportModel().find_current_week()
                        last_ex_model = ExecutiveReportModel().find_last_week()
                        menu_05_01_ex_rpt_show_week.replyMsg(reply_token, curr_ex_model, last_ex_model,
                                                             CHANNEL_ACCESS_TOKEN)

                # elif message in DEMO_APP:  # Demo App
                #     menu_demo_app.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                # elif message in CHECK_PM:  # CHECK PM 2.5
                elif message == DASHBOARD_CARD:
                    menu_07_01_dashboard.replyMsg(reply_token, userId, CHANNEL_ACCESS_TOKEN)
                elif message == CHECK_PM:
                    share_location.quickreplymsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                elif message == HOT_ISSUE:
                    menu_06_01_hotissue.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                elif message in VIRUS:
                    virus = VirusCoronaModel().find_all()
                    virus_totl = VirusCoronaModel().get_TotalCase()
                    print(virus_totl[0], virus_totl[1], virus_totl[2])
                    virus_corona_stat.replyMsg(reply_token, virus,
                                               virus_totl[0],
                                               virus_totl[1],
                                               virus_totl[2],
                                               CHANNEL_ACCESS_TOKEN)
                elif message in REPLY_WORDING:
                    reply_msg = DEFAULT_REPLY_WORDING
                    # Reply Message Default Post API
                    chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
            else:
                # print("not found")
                if re.match(REGISTER_MSG, message):
                    register_flag = 'Y'
                    txt_temp = msg_text
                    text = txt_temp.replace('register=>emp:', '').strip().replace('password:', '').strip()
                    value = text.split(',')
                    register_empid = value[0].strip().lower()
                    register_email = value[1].strip().lower()
                    # print(register_empid, register_email)

                    # reply_msg = "We have received your registration. Please wait for confirmation within 2 minute."
                    reply_msg = "We have received your registration. Within 2 minutes, \
                                you will be able to use CRM chatbot."
                    chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                    # chatbot_register.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                    # print("Register Msg")
                else:
                    # reply_msg = "You are not authorized to access this menu. please register from link line://app/1653377835-peowRY0O"
                    # chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                    if not groupId:
                        if not re.match(REGISTER_REJECT_MSG, message):
                            chatbot_register.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
        elif msg_type == 'image':  # Image Upload to Line Bot
            image_id = payload['events'][0]['message']['id']
            contentProvider = payload['events'][0]['message']['contentProvider']['type']
            print(f"{image_id} , {contentProvider}")
        elif msg_type == 'location':
            location_id = payload['events'][0]['message']['id']
            address = payload['events'][0]['message']['address']
            latitude = payload['events'][0]['message']['latitude']
            longitude = payload['events'][0]['message']['longitude']
            # print(f"{location_id}, {latitude}, {longitude}")

            # GET PM2.5 Value from API xx
            city, state, country, pm_val, temperature, icon_weather = check_pm_airvisual.getpm(latitude, longitude)
            header = "{0}, {1}, {2}".format(city, state, country)
            menu_06_01_pm_value.replyMsg(reply_token, header, pm_val, CHANNEL_ACCESS_TOKEN)
        elif msg_type == 'postback':
            param_data = payload['events'][0]['postback']['data']
            print(param_data)
            richmenuId = None
            if param_data == 'next':
                richmenuId = RICH_MENU_SECOND
            elif param_data == 'back':
                richmenuId = RICH_MENU_MAIN
            else:
                pass

            chatbot_rich_menu.replyMsg(userId=userId,
                                       richMenuId=richmenuId,
                                       line_aceess_token=CHANNEL_ACCESS_TOKEN)
            # param_data = payload['events'][0]['postback']['data']
            # param_date = payload['events'][0]['postback']['params']['date']
            # date_val = param_date.replace("-", "").strip()
            # # print(param_data, date_val)
            # if re.match(LL_MSG_AC_DAILY, param_data):  # Actual income select Daily by Project
            #     values = ActualIncomeByProjModel().find_by_date(date_val)
            #     menu_04_01_actual_income_show_daily.replyMsg(reply_token, None,
            #                                                  values,
            #                                                  param_date,
            #                                                  CHANNEL_ACCESS_TOKEN)
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
                            register_flag, register_empid, register_email)

        return {"message": "Register Line Push and Reply Message Successful"}, 201
