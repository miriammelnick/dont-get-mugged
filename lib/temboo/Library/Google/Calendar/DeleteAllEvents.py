
###############################################################################
#
# DeleteAllEvents
# Delete all events from a specified calendar. Note that this operation can't be undone.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteAllEvents(Choreography):

    """
    Create a new instance of the DeleteAllEvents Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Calendar/DeleteAllEvents')


    def new_input_set(self):
        return DeleteAllEventsInputSet()

    def _make_result_set(self, result, path):
        return DeleteAllEventsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteAllEventsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteAllEvents
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteAllEventsInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the CalendarID input for this choreography. ((optional, string) The ID for the primary calendar to delete. Defaults to "primary" which corresponds to the primary calendar of the authenticated user.)
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
        Set the value of the RefreshToken input for this choreography. ((required, string) The refresh token retrieved in the last step of the OAuth process. This is used whenever your access token expires.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteAllEvents choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteAllEventsResultSet(ResultSet):
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

class DeleteAllEventsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteAllEventsResultSet(response, path)
