#!/usr/bin/env python3

uacTable = { 1: "SCRIPT",
             2: "ACCOUNTDISABLE",
             8: "HOMEDIR_REQUIRED",
             16: "LOCKOUT",
             32: "PASSWD_NOTREQD",
             64: "PASSWD_CANT_CHANGE",
             128: "ENCRYPTED_TEXT_PWD_ALLOWED",
             256: "TEMP_DUPLICATE_ACCOUNT",
             512: "NORMAL_ACCOUNT",
             2048: "INTERDOMAIN_TRUST_ACCOUNT",
             4096: "WORKSTATION_TRUST_ACCOUNT",
             8192: "SERVER_TRUST_ACCOUNT",
             65536: "DONT_EXPIRE_PASSWORD",
             131072: "MNS_LOGON_ACCOUNT",
             262144: "SMARTCARD_REQUIRED",
             524288: "TRUSTED_FOR_DELEGATION",
             1048576: "NOT_DELEGATED",
             2097152: "USE_DES_KEY_ONLY",
             4194304: "DONT_REQ_PREAUTH",
             8388608: "PASSWORD_EXPIRED",
             16777216: "TRUSTED_TO_AUTH_FOR_DELEGATION",
             67108864: "PARTIAL_SECRETS_ACCOUNT",
            }

def getRights(uacnum):
    res = []
    for flag in uacTable.keys():
        if flag & uacnum > 0:
            res.append(uacTable[flag])
    return res
