
###############################################################################
#
# UpdateCalendar
# Updates the metadata for a calendar.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateCalendar(Choreography):

    """
    Create a new instance of the UpdateCalendar Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Calendar/UpdateCalendar')


    def new_input_set(self):
        return UpdateCalendarInputSet()

    def _make_result_set(self, result, path):
        return UpdateCalendarResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateCalendarChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateCalendar
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateCalendarInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the CalendarID input for this choreography. ((required, string) The ID for the calendar to update.)
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
        Set the value of the NewDescription input for this choreography. ((optional, string) The new description for the calendar to update.)
        """
        def set_NewDescription(self, value):
            InputSet._set_input(self, 'NewDescription', value)

        """
        Set the value of the NewLocation input for this choreography. ((optional, string) The new location for the calendar to update.)
        """
        def set_NewLocation(self, value):
            InputSet._set_input(self, 'NewLocation', value)

        """
        Set the value of the NewSummary input for this choreography. ((required, string) The new summary for the calendar to update.)
        """
        def set_NewSummary(self, value):
            InputSet._set_input(self, 'NewSummary', value)

        """
        Set the value of the NewTimezone input for this choreography. ((optional, string) The new timezone for the calendar to update.)
        """
        def set_NewTimezone(self, value):
            InputSet._set_input(self, 'NewTimezone', value)

        """
        Set the value of the RefreshToken input for this choreography. ((required, string) The refresh token retrieved in the last step of the OAuth process. This is used whenever your access token expires.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateCalendar choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateCalendarResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Google. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "UpdateCalendar" output from this choreography execution. (The request template with appropriate inputs passed.)
        """
        def get_UpdateCalendar(self):
            return self._output.get('UpdateCalendar', None)
        """
        Retrieve the value for the "AccessToken" output from this choreography execution. ((required, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def get_AccessToken(self):
            return self._output.get('AccessToken', None)

class UpdateCalendarChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateCalendarResultSet(response, path)
