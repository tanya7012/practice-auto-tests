import time
fix = init("FIX_1")

nos1=fix.send("NEW_ORDER_SINGLE", {"Symbol" : "AAPL", "ClOrdID" : generate_clordid(15), "Side" : "2", "Price":"400", "OrderQty":"50", "ClientID" : "USER1", "OrdType" : "2", "TimeInForce": "1"})
er1=fix.expect("EXECUTION_REPORT", {"Symbol": nos1[0]["Symbol"]}, timeout=3)
report("Get execution report",er1,group="Test case group 1",exit_on_failure=False)

nos2=fix.send("NEW_ORDER_SINGLE", {"Symbol" : "AAPL", "ClOrdID" : generate_clordid(15),"Price": "400", "Side" : "1", "OrderQty" : "50", "ClientID" : "USER1", "OrdType": "2", "TimeInForce": "1"})
er2=fix.expect("EXECUTION_REPORT", {"Symbol": nos2[0]["Symbol"]}, timeout=3)
report("Get execution report",er2,group="Test case group 1",exit_on_failure=False)

nos3=fix.send("NEW_ORDER_SINGLE", {"Symbol" : "AAPL", "ClOrdID" : generate_clordid(15), "Side" : "2" ,"Price":"360", "OrderQty" : "50", "ClientID" : "USER1", "OrdType" : "2", "TimeInForce": "1"})
er3=fix.expect("EXECUTION_REPORT", {"Symbol": nos3[0]["Symbol"]}, timeout=3)
report("Get execution report",er3,group="Test case group 1",exit_on_failure=False)

nos4=fix.send("NEW_ORDER_SINGLE", {"Symbol" : "AAPL", "ClOrdID" : generate_clordid(15), "Side" : "1", "Price":"360","StopPx":"350", "OrderQty" : "100", "ClientID" : "USER1", "OrdType" :"4", "TimeInForce": "1"})
er4=fix.expect("EXECUTION_REPORT", {"Symbol": nos4[0]["Symbol"]}, timeout=3)
report("Get execution report",er4,group="Test case group 1",exit_on_failure=False)

time.sleep(20)

nos5=fix.send("NEW_ORDER_SINGLE", {"Symbol": "AAPL", "ClOrdID": generate_clordid(15), "Side": "2","Price": "360", "OrderQty": "50", "ClientID": "USER1", "OrdType": "2", "TimeInForce": "1"})
er5=fix.expect("EXECUTION_REPORT", {"Symbol": nos5[0]["Symbol"]}, timeout=3)
report("Get execution report", er5, group = "Test case group 1", exit_on_failure=False)

