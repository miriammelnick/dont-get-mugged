
###############################################################################
#
# CampaignSend
# Generate a CSV file for sending a campaign.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CampaignSend(Choreography):

    """
    Create a new instance of the CampaignSend Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/ObadMobileMarketing/CampaignSend')


    def new_input_set(self):
        return CampaignSendInputSet()

    def _make_result_set(self, result, path):
        return CampaignSendResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CampaignSendChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CampaignSend
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CampaignSendInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Private Key for 1 unique distributor - provided by Obad Mobile Marketing)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the CampaignID input for this choreography. ((integer) The ID for the campaign you want to send)
        """
        def set_CampaignID(self, value):
            InputSet._set_input(self, 'CampaignID', value)

        """
        Set the value of the ClientID input for this choreography. ((integer) Private Key for 1 unique customer to connect with - provided by Obad Mobile Marketing)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the Endpoint input for this choreography. ((string) The base URL for the server you want to access (i.e. http://10.10.10.1). Set this to the appropriate host for the demo sandbox or production.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the Type input for this choreography. ((optional, string) The type of campaign you're sending.  Can be sms, mail, or smsmail. Defaults to sms.)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)


"""
A ResultSet with methods tailored to the values returned by the CampaignSend choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CampaignSendResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Obad)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CampaignSendChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CampaignSendResultSet(response, path)
