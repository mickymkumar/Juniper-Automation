# Notes

## Steps 
1. Bring up the infrastructure. for example... With  docker
2. Upgrade to the latest code using development branch
3. Add a subscriber in orch8r and Bevo
4. verify and test


- Process
+

### Bring up the infrastructure

## Automation Steps
- Allow user to pass the image tag to be tested. 
    - Registry URL where the Image exists.
    - Image version to be downloaded. 
- If user is not providing the image tag consider to build the image from the source. 
- Use the user provided image tag or locally build image tag to provision the infrastructure along with the flask server to mimic bevo. 
- Integrate the gw with orc8r 
- Add user in NMS dashboard. 
- Test, if the user is visible 
    - Using the GW cli
    - Using the swagger of bevo. (here flask server)

## Automation table
| Step | User Input | Action | Expected Output | Actual Output | Pass/Fail |
|------|------------|--------|------------------|---------------|-----------|
|1A. Allow user to pass the image tag to be tested. ||||||
|1B. Build the image from source if no image tag provided. ||||||
|2. build image tag to provision the infrastructure along with the flask server to mimic bevo. ||||||
|3. Integrate the gw with Orchestrator. ||||||
|4. Add the user in NMS Dashboard. ||||||
