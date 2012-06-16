
###############################################################################
#
# GetNotificationBySID
# Get comprehensive log information for a specified Notification SID. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetNotificationBySID(Choreography):

    """
    Create a new instance of the GetNotificationBySID Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twilio/GetNotificationBySID')


    def new_input_set(self):
        return GetNotificationBySIDInputSet()

    def _make_result_set(self, result, path):
        return GetNotificationBySIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNotificationBySIDChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetNotificationBySID
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetNotificationBySIDInputSet(InputSet):
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
        Set the value of the NotificationSID input for this choreography. ((required, string) Enter the SID of the notification resource to be retrieved.)
        """
        def set_NotificationSID(self, value):
            InputSet._set_input(self, 'NotificationSID', value)


"""
A ResultSet with methods tailored to the values returned by the GetNotificationBySID choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetNotificationBySIDResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Twilio.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetNotificationBySIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetNotificationBySIDResultSet(response, path)
