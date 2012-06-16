
###############################################################################
#
# DeleteEvent
# Delete a specific event from a specified calendar.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteEvent(Choreography):

    """
    Create a new instance of the DeleteEvent Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Calendar/DeleteEvent')


    def new_input_set(self):
        return DeleteEventInputSet()

    def _make_result_set(self, result, path):
        return DeleteEventResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteEventChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteEvent
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteEventInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the CalendarID input for this choreography. ((required, string) The ID for the calendar to delete.)
        """
        def set_CalendarID(self, value):
            InputSet._set_input(self, 'CalendarID', value)

        """
        Set the value of the ClientID input for this choreography. ((required, string) The client ID provided by Google when you register your application.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the ClientSecret input for this choreography. ((required, string) The client secret provided by Google when you registered your application.)
        """
        def set_ClientSecret(self, value):
            InputSet._set_input(self, 'ClientSecret', value)

        """
        Set the value of the EventID input for this choreography. ((required, string) The unique ID for the event to delete.)
        """
        def set_EventID(self, value):
            InputSet._set_input(self, 'EventID', value)

        """
        Set the value of the RefreshToken input for this choreography. ((required, string) The refresh token retrieved in the last step of the OAuth process. This is used whenever your access token expires.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteEvent choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteEventResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (No content is returned for delete calendar operations.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "AccessToken" output from this choreography execution. ((required, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def get_AccessToken(self):
            return self._output.get('AccessToken', None)

class DeleteEventChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteEventResultSet(response, path)
