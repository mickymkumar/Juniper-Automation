1. fix the post - checking... 
2. delete function - On Hold
3. generate the reports - e.x reports/datetime/date-time-filename.txt
4. yml format [done] & connnections  -> done tomorrow
5. APN - checking

5G:
- A few test cases
- We create 3 reports: syslogs, mme logs, PCAP
-N1, N2 N3

Overview
1. Dynamic values/static values
2. user define the Dynamic values
3. scripts runs


test
 - api 
   - apn
   - network
    - test1:
      - get
      - post
      - delete
    - test2:
      - get


   - polcydb
- 5G
runner - folders/reports



test
 - api
  - get
  - post
  - put
  - delete

1. Ask are we showing framework [next week] or test case[we can show Get APN]?
2. Who are we showing it to? - Suresh, Juniper?
3.


git reset --hard HEAD
git pull


test_API_M1_LTE_TC0003_APN_Delete_APN
test_API_M2_Events_TC0003_APN_Delete_APN
test_API_M3_Subscriber_TC0003_APN_Delete_APN
test_API_M4_Policy_TC0003_APN_Delete_APN
test_Bevo_M3_counter_TC0003_APN_Delete_APN


5G
Verification access VM
- Password login to the vm - **Tapas/yogesh Discussion on password VM**
Value Path location:
- /var/opt/magma/configs/
Which files will be affected.
Writing the test cases
verifying how to create mme, syslogs, pcap

if path_file == '222' and user_config == '222':
   print("Passed"")
pip install pyshark
1. step 1 - Setup:
   2. Variable path
   3. os module - syslogs
   4. os module - mme logs
   5. Go in the the logging folder and save with date and time  subfolder [syslogs,mme, pcaps, API]
2. Step 2 - Based test cases [Change]
   3. NGSetup test case:
      4. test_NgSetup_request
      5. NGSetup Response
6. Step 3: Teardown:
   7. 3 second wait timer
   8. close logs
Create a file with possibles values.