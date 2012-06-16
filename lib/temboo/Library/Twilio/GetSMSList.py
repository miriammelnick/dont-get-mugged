
###############################################################################
#
# GetSMSList
# Retrieves a list of SMS messages from your Twilio account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetSMSList(Choreography):

    """
    Create a new instance of the GetSMSList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twilio/GetSMSList')


    def new_input_set(self):
        return GetSMSListInputSet()

    def _make_result_set(self, result, path):
        return GetSMSListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSMSListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetSMSList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetSMSListInputSet(InputSet):
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
        Set the value of the DateSent input for this choreography. ((optional, date) A date in YYYY-MM-DD format. If you use this input, the Choreo will retrieve only messages sent on this date.)
        """
        def set_DateSent(self, value):
            InputSet._set_input(self, 'DateSent', value)

        """
        Set the value of the From input for this choreography. ((optional, string) If used, the Choreo will only retrieve messages sent from this phone number.)
        """
        def set_From(self, value):
            InputSet._set_input(self, 'From', value)

        """
        Set the value of the To input for this choreography. ((optional, string) If used, the Choreo will only retrieve messages sent to this phone number.)
        """
        def set_To(self, value):
            InputSet._set_input(self, 'To', value)


"""
A ResultSet with methods tailored to the values returned by the GetSMSList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetSMSListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Twilio.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetSMSListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetSMSListResultSet(response, path)
