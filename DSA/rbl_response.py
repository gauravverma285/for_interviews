# for IMPS ((((Initiated))))

{
    "Single_Payment_Corp_Resp":{
        "Header":{
            "TranID":"1730289077",
            "Corp_ID":"SINGHTKLTD",
            "Maker_ID":"M005",
            "Checker_ID":"C003",
            "Approver_ID":"A003",
            "Status":"Initiated",
            "Error_Cde":{},
            "Error_Desc":{}},
            "Body":{
                "RefNo":"SPSINGHTKLTD1730289077",
                "UTRNo":"RATNH24197288086",
                "PONum":"000284315865",
                "Ben_Acct_No":"109566016481",
                "Amount":"200000.01",
                "BenIFSC":"DNSB0000021",
                "Txn_Time":"2024-07-15 12:37:20.780181"
                },
                "Signature":{
                    "Signature":"Signature"
                    }
                    }}

# for IMPS (((((Failure)))))

{"Single_Payment_Corp_Resp":{
    "Header":{
        "TranID":"9533294526",
        "Corp_ID":"SINGHTKLTD",
        "Maker_ID":"M005",
        "Checker_ID":"C003",
        "Approver_ID":"A003",
        "Status":"Failure",
        "Resp_cde":"CZ",
        "Error_Desc":"FAILURE Test Case Not Found"},
        "Body":{
            "channelpartnerrefno":"IMPSSINGHTKLTD9533294526",
            "RRN":"420801000140"},
            "Signature":{
                "Signature":"Signature"}
                }}

# for NEFT ((((In Progress))))

{"Single_Payment_Corp_Resp":{
    "Header":{
        "TranID":"9519449150",
        "Corp_ID":"SINGHTKLTD",
        "Maker_ID":"M005",
        "Checker_ID":"C003",
        "Approver_ID":"A003",
        "Status":"In Progress",
        "Error_Cde":"","Error_Desc":""
        },
        "Signature":{
            "Signature":"Signature"}}}

# for NEFT ((((Initiated))))

{"Single_Payment_Corp_Resp":{
    "Header":{
        "TranID":"1272004503",
        "Corp_ID":"SINGHTKLTD",
        "Maker_ID":"M005",
        "Checker_ID":"C003",
        "Approver_ID":"A003",
        "Status":"Initiated",
        "Error_Cde":{},
        "Error_Desc":{}
        },
        "Body":{
            "RefNo":"SPSINGHTKLTD1272004503",
            "UTRNo":"RATNN24200329588",
            "PONum":"000284357490",
            "Ben_Acct_No":"109566016481",
            "Amount":"200.01",
            "BenIFSC":"DNSB0000021",
            "Txn_Time":"2024-07-18 15:31:37.591324"
            },
            "Signature":{
                "Signature":"Signature"}}}


# for RTGS  ((((In Progress))))

{"Single_Payment_Corp_Resp":{
    "Header":{
        "TranID":"2018893726",
        "Corp_ID":"SINGHTKLTD",
        "Maker_ID":"M005",
        "Checker_ID":"C003",
        "Approver_ID":"A003",
        "Status":"In Progress",
        "Error_Cde":"",
        "Error_Desc":""
        },
        "Signature":{"Signature":"Signature"}}}


# for RTGS  ((((Initiated))))

{"Single_Payment_Corp_Resp":{
    "Header":{
        "TranID":"8797876441",
        "Corp_ID":"SINGHTKLTD",
        "Maker_ID":"M005",
        "Checker_ID":"C003",
        "Approver_ID":"A003",
        "Status":"Initiated",
        "Error_Cde":{},
        "Error_Desc":{}
        },
        "Body":{
            "RefNo":"SPSINGHTKLTD8797876441",
            "UTRNo":"RATNH24200329590",
            "PONum":"000284357492",
            "Ben_Acct_No":"109566016481",
            "Amount":"200000.01",
            "BenIFSC":"DNSB0000021",
            "Txn_Time":"2024-07-18 16:17:01.544118"
            },
            "Signature":{"Signature":"Signature"}}}


# FT Failure

{"Single_Payment_Corp_Resp":{
    "Header":{
        "TranID":"8450362108",
        "Corp_ID":"SINGHTKLTD",
        "Maker_ID":"M005",
        "Checker_ID":"C003",
        "Approver_ID":"A003",
        "Status":"Failure",
        "Error_Cde":"162",
        "Error_Desc":"The account does not exist."},
        "Signature":{
            "Signature":"Signature"}
            }}



# NEFT success ------> status fetched 
# RTGS success ------> status fetched 



# eror 500
# {"httpCode":"500","httpMessage":"Internal Server Error","moreInformation":"Internal Error"}