"""Utility module for IOT SDK operations."""
import os
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from utility.logger_utility import LoggerUtility
from utility.common_constants import EnvironmentVariables, Constants


class IotUtility:
    """Class to perform IoT operations."""

    def __init__(self):
        """Class constructor."""
        try:
            client_id = os.environ[EnvironmentVariables.IOT-CLIENT-ID]
            port_no = int(os.environ[EnvironmentVariables.PORT])
            iot_endpoint = os.environ[EnvironmentVariables.IOT_ENDPOINT]
        except KeyError as port_not_configured:
            # Use default port if environment variable is not set
            LoggerUtility.log_warning(str(port_not_configured) + " not configured, using default port!")
            port_no = Constants.IOT_DEFAULT_PORT_NO

    def set_certificate_authentication_id(self, client_id):
        """Set Certificate Client ID from Constants."""
        MQTT_Certificate_Client = AWSIoTMQTTClient(client_id)
        return MQTT_Certificate_Client
        
    def set_certificate_authentication_id(self, client_id):
        """Set Certificate Client ID from Constants."""
        MQTT_Certificate_Client = AWSIoTMQTTClient(client_id)
        return MQTT_Certificate_Client
