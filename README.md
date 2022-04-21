# RESTMethod

This sample app demonstrates how to use an app *REST method* to populate a dashboard item in QRadar. The app is simple
and uses Flask and Jinja to render a HTML page with a dropdown list of QRadar Ariel database names, retrieved from the
QRadar API using QPyLib. This list of QRadar Ariel database names visible as a dashboard item.

## Running this app

You can package this app and deploy it by executing in this directory:

```bash
qapp package -p app.zip
```

and

```bash
qapp deploy -p app.zip -q <qradar console ip> -u <qradar user>
```

##There are some configurations you need to do on your Mac
### Certificates for authentication with QRAdar
  - your cert should be in ~/.qradar_app_sdk

### Add the entry for the Qradar host in hosts file
- It should be in format `ipAddress FQDN`
  - ```bash 
    cat /etc/hosts | grep .50 
    x.x.x.50 vm592087.com 
    ```

###Use the curl command to check if network is an issue - 
  
  - ```bash
    curl -S -X GET -u admin -H 'Range: items=0-49' -H 'Version: 16.0' -H 'Accept: application/json' --cacert ca-bundle.crt 'https://x.x.x50/api/ariel/databases'
    ```
