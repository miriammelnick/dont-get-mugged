
###############################################################################
#
# GetAllNotifications
# Return a list of all notifications generated for a specified account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetAllNotifications(Choreography):

    """
    Create a new instance of the GetAllNotifications Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twilio/GetAllNotifications')


    def new_input_set(self):
        return GetAllNotificationsInputSet()

    def _make_result_set(self, result, path):
        return GetAllNotificationsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAllNotificationsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetAllNotifications
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetAllNotificationsInputSet(InputSet):
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
        Set the value of the LogLevel input for this choreography. ((optional, integer) Specify the log level by entering: 0 for ERROR, 1 for WARNING.)
        """
        def set_LogLevel(self, value):
            InputSet._set_input(self, 'LogLevel', value)

        """
        Set the value of the MessageDate input for this choreography. ((optional, string) Filter notifications by date.  Dates should be formatted as follows: YYYY-MM-DD.  Dates before, at, or after a specified date can be entered using inequality operators: >=YYYY-MM-DD)
        """
        def set_MessageDate(self, value):
            InputSet._set_input(self, 'MessageDate', value)


"""
A ResultSet with methods tailored to the values returned by the GetAllNotifications choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetAllNotificationsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Twilio.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetAllNotificationsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAllNotificationsResultSet(response, path)
