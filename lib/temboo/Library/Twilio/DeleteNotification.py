
###############################################################################
#
# DeleteNotification
# Delete a notification from the account log.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteNotification(Choreography):

    """
    Create a new instance of the DeleteNotification Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twilio/DeleteNotification')


    def new_input_set(self):
        return DeleteNotificationInputSet()

    def _make_result_set(self, result, path):
        return DeleteNotificationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteNotificationChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteNotification
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteNotificationInputSet(InputSet):
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
A ResultSet with methods tailored to the values returned by the DeleteNotification choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteNotificationResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Twilio.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteNotificationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteNotificationResultSet(response, path)
