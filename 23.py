fix = init("FIX_1")

nos1=fix.send("NEW_ORDER_SINGLE", {"Symbol" : "AAPL", "ClOrdID" : "thisID", "Side" : "1", "Price":"400", "OrderQty" : "50", "ClientID" : "USER1", "OrdType" : "2", "TimeInForce": "1"})
er1=fix.expect("EXECUTION_REPORT", {"Symbol": nos1[0]["Symbol"]}, timeout=3)
report("Get execution report",er1,group="Test case group 1",exit_on_failure=False)

nos2=fix.send("ORDER_CANCEL_REQUEST", {"Symbol" : "AAPL", "ClOrdID" : "kdklnfvdon","OrigClOrdID": "thisID", "Side" : "1"})
er2=fix.expect("EXECUTION_REPORT", {"Symbol": nos2[0]["Symbol"]}, timeout=3)
report("Get execution report",er2,group="Test case group 1",exit_on_failure=False)

nos3=fix.send("NEW_ORDER_SINGLE", {"Symbol" : "AAPL", "ClOrdID" : generate_clordid(15), "Side" : "2" , "OrderQty" : "50", "ClientID" : "USER1", "OrdType" : "1", "TimeInForce": "1"})
er3=fix.expect("EXECUTION_REPORT", {"Symbol": nos3[0]["Symbol"]}, timeout=3)
report("Get execution report",er3,group="Test case group 1",exit_on_failure=False)
