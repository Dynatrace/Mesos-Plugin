# Mesos Plugin

## Installation from pre-built binaries
* Download the [pre-built binaries](https://github.com/wmsegar/Mesos-Plugin/blob/master/custom.python.mesos_plugin.zip?raw=true)
* Extract the contents of the ```custom.python.mesos_plugin.zip``` into ```/opt/dynatrace/oneagent/plugin_deployment```
  - Make sure you don't extract by creating an extra folder name after the zip archive
  - Among other files you should now be able to see ```/opt/dynatrace/oneagent/plugin_deployment/custom.python.mesos_plugin/plugin.json```
* Restart your Dynatrace OneAgent
  - Usually the command for that is ```sudo service onagent restart```
* Log into your Dynatrace tenant and navigate to ```Settings / Monitored Technologies```
* Select the tab ```Custom Plugins```
* Click on the button ```Upload Plugin``` and select your local ```custom.python.mesos_plugin.zip```
* Click on the new entry ```custom.python.mesos_plugin```
* Configure the user credentials, server, port and Mesos API URI.  By default the plugin with attempt to connect to the Mesos API using the following: ```http://localhost:80/metrics/snapshot```
* Click on the button ```Upgrade Now```

Within a couple of minutes you should find additional metrics getting reported for a process called ```mesosphere.marathon.Main``` for the host you have deployed the plugin on.
