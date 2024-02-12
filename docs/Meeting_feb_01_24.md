- Allow user to pass the image tag to be tested. 
    - Registry URL where the Image exists.
    * ask registry url
    - Image version to be downloaded. 
     * check the tags? - dvelopment?
     * yogesh,  check to use docker or kubernetes? -> that  how to download it and pick up develoment if  needed.
- If user is not providing the image tag consider to build the image from the source. 

- Use the user provided image tag or locally build image tag to provision the infrastructure along with the flask server to mimic bevo. 
* mehul, share around flask server. https://github.com/wavelabsai/magma-general-utility/tree/master/pmn-systems-confs/flask-api-handler 


- Integrate the gw with orc8r 

- Add the network 
- Add the gateway, (verification step)
- Add user(subscriber) in NMS dashboard. 
* this one I have
- Test, if the user is visible 
    - Using the GW cli
    * work with naresh
    - Using the swagger of bevo. (here flask server)
    * Arun, can help here with this


- one orch8r, gateway, creating network and sync to orch8r.