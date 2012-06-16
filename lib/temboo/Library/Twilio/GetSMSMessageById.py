
###############################################################################
#
# GetSMSMessageById
# Retrieves a specific SMS from Twilio by allowing you to specify a message ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetSMSMessageById(Choreography):

    """
    Create a new instance of the GetSMSMessageById Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twilio/GetSMSMessageById')


    def new_input_set(self):
        return GetSMSMessageByIdInputSet()

    def _make_result_set(self, result, path):
        return GetSMSMessageByIdResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSMSMessageByIdChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetSMSMessageById
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetSMSMessageByIdInputSet(InputSet):
        """
        Set the value of the AccountSID input for this choreography. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        def set_AccountSID(self, value):
            InputSet._set_input(self, 'AccountSID', value)

        """
        Set the value of the AuthToken input for this choreography. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        def set_AuthToken(self, value):
            InputSet._set_input(self, 'AuthToken', value)

        """
        Set the value of the SMSMessageSid input for this choreography. ((required, string) The unique ID for the Twilio message you want to retrieve.)
        """
        def set_SMSMessageSid(self, value):
            InputSet._set_input(self, 'SMSMessageSid', value)


"""
A ResultSet with methods tailored to the values returned by the GetSMSMessageById choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetSMSMessageByIdResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Twilio.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetSMSMessageByIdChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetSMSMessageByIdResultSet(response, path)
