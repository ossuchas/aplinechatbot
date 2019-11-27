import traceback
from flask_restful import Resource
from flask import request
import re

from libs import chatbot_helper, log_linechatbot as logs, \
    sale_accum_month, beacon_helper,  \
    menu_01_sale_timeline as m1_SDH, \
    leadlag_bg_all, leadlag_bg_project, \
    menu_02_01_ll_sdh_subbg, menu_02_01_ll_sdh_period, \
    menu_01_01_ll_allbg_period, menu_01_01_ll_allbg_period_show_Q, \
    menu_01_01_ll_allbg_period_show_M, menu_01_01_ll_allbg_period_show_W, \
    menu_01_01_ll_allbg_period_show_Y, menu_01_01_ll_allbg_period_show_A, \
    menu_05_ap_phonebook, menu_actual_income_ac_Q, menu_executive_report, \
    menu_01_01_ll_allbg_sel_bg

from config import CHANNEL_ACCESS_TOKEN, REPLY_WORDING, \
    REPLY_SALCE_ACCM_B_M_WORDING, REPLY_SALCE_ACCM_C_M_WORDING, \
    DEFAULT_REPLY_WORDING, \
    MENU_01_VIP, MENU_01_VIP_BG, \
    MENU_01_01_SDH, \
    LL_MSG_All, LL_MSG_PROJ, LL_MSG_SUB, \
    LL_MSG_SUB_PERIOD, LL_MSG_ALLBG_PERIOD, \
    LL_MSG_APPHONEBOOK, LL_MSG_APPHONEBOOK2, \
    AC_ACTUAL_INCOME, EXECUTIVE_REPORT


from models.chatbot_mst_user import MstUserModel
from models.log_linechatbot import LogChatBotModel
from models.crm_line_actual_income import ActualIncomeModel
from models.crm_line_ll_data import LeadLagModel


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

        try:
            groupId = payload['events'][0]['source']['groupId']
            userId = payload['events'][0]['source']['userId']
            # print(userId, groupId)
        except:
            userId = payload['events'][0]['source']['userId']

        if events_type == 'message':
            msg_type = payload['events'][0]['message']['type']
        else:
            msg_type = 'beacon'

        reply_msg = None

        if msg_type == 'text':
            msg_text = payload['events'][0]['message']['text']
            message = msg_text

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
            elif message in MENU_01_01_SDH:
                m1_SDH.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
            # Lead Lag
            elif message in LL_MSG_All:
                leadlag_bg_all.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
            elif message in LL_MSG_SUB:  # menu_02_01_ll_sdh_subbg
                menu_02_01_ll_sdh_subbg.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
            elif re.match(LL_MSG_PROJ, message):  # proj:
                value = message.split(',')
                project = value[0].split(':')
                peroid = value[1].split(':')
                leadlag_bg_project.replyMsg(reply_token, project[1].strip(), peroid[1].strip()[0], CHANNEL_ACCESS_TOKEN)
            # Period Select ALL BG
            elif re.match(LL_MSG_ALLBG_PERIOD, message):  # LL BY BG Period
                # peroid = message.replace(LL_MSG_ALLBG_PERIOD, "").strip()[0]
                peroid = message.replace(LL_MSG_ALLBG_PERIOD, "").strip()
                bg = re.match(r"[^[]*\[([^]]*)\]", peroid).groups()[0]
                if peroid[0] == 'Q':  # Quarter
                    menu_01_01_ll_allbg_period_show_Q.replyMsg(reply_token, bg, CHANNEL_ACCESS_TOKEN)
                elif peroid[0] == 'M':  # Month
                    menu_01_01_ll_allbg_period_show_M.replyMsg(reply_token, bg, CHANNEL_ACCESS_TOKEN)
                elif peroid[0] == 'W':  # Week
                    ll_model = LeadLagModel().find_by_bg_period(bg, peroid[0])
                    menu_01_01_ll_allbg_period_show_W.replyMsg(reply_token, bg, ll_model, CHANNEL_ACCESS_TOKEN)
                elif peroid[0] == 'Y':  # Yesterday
                    menu_01_01_ll_allbg_period_show_Y.replyMsg(reply_token, bg, CHANNEL_ACCESS_TOKEN)
                elif peroid[0] == 'A':  # As of Current
                    menu_01_01_ll_allbg_period_show_A.replyMsg(reply_token, bg, CHANNEL_ACCESS_TOKEN)
            # Period Select by Sub BG
            elif re.match(LL_MSG_SUB_PERIOD, message):
                menu_02_01_ll_sdh_period.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
            # AP PhoneBook Menu 5
            elif (re.match(LL_MSG_APPHONEBOOK, message)) or (re.match(LL_MSG_APPHONEBOOK2, message)):
                menu_05_ap_phonebook.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
            elif message in REPLY_SALCE_ACCM_B_M_WORDING:
                sale_accum_month.replyMsg(reply_token, reply_msg, "-1", CHANNEL_ACCESS_TOKEN)
            elif message in REPLY_SALCE_ACCM_C_M_WORDING:
                sale_accum_month.replyMsg(reply_token, reply_msg, "0", CHANNEL_ACCESS_TOKEN)
            elif message in AC_ACTUAL_INCOME:
                actual_income = ActualIncomeModel().find_all()
                menu_actual_income_ac_Q.replyMsg(reply_token, actual_income, CHANNEL_ACCESS_TOKEN)
            elif message in EXECUTIVE_REPORT:
                actual_income = ActualIncomeModel().find_all()
                menu_executive_report.replyMsg(reply_token, actual_income, CHANNEL_ACCESS_TOKEN)
            elif message in REPLY_WORDING:
                reply_msg = DEFAULT_REPLY_WORDING

                # Reply Message Default Post API
                chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
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
                            beacon_hwid, beacon_dm, beacon_type)

        return {"message": "Register Line Push and Reply Message Successful"}, 201

