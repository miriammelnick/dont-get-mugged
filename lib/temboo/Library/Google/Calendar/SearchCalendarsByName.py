
###############################################################################
#
# SearchCalendarsByName
# Retrieves information about a calendar including the id with a given calendar name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchCalendarsByName(Choreography):

    """
    Create a new instance of the SearchCalendarsByName Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Calendar/SearchCalendarsByName')


    def new_input_set(self):
        return SearchCalendarsByNameInputSet()

    def _make_result_set(self, result, path):
        return SearchCalendarsByNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchCalendarsByNameChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchCalendarsByName
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchCalendarsByNameInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the CalendarName input for this choreography. ((required, string) The name of the calendar that you want to retrieve information for. Note that if there are multiple calendars with the same name, only the first one will be returned.)
        """
        def set_CalendarName(self, value):
            InputSet._set_input(self, 'CalendarName', value)

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
        Set the value of the Count input for this choreography. ((optional, integer) The maximum number of calendars to search by name. The default is 15.)
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the RefreshToken input for this choreography. ((required, string) The refresh token retrieved in the last step of the OAuth process. This is used whenever your access token expires.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)


"""
A ResultSet with methods tailored to the values returned by the SearchCalendarsByName choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchCalendarsByNameResultSet(ResultSet):
        """
        Retrieve the value for the "AccessToken" output from this choreography execution. ((required, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def get_AccessToken(self):
            return self._output.get('AccessToken', None)
        """
        Retrieve the value for the "CalendarDescription" output from this choreography execution. ((string) The calendar description parsed from the Google response.)
        """
        def get_CalendarDescription(self):
            return self._output.get('CalendarDescription', None)
        """
        Retrieve the value for the "CalendarId" output from this choreography execution. ((string) The calendar id parsed from the Google response.)
        """
        def get_CalendarId(self):
            return self._output.get('CalendarId', None)
        """
        Retrieve the value for the "CalendarSummary" output from this choreography execution. ((string) The summary or calendar name parsed from the Google response.)
        """
        def get_CalendarSummary(self):
            return self._output.get('CalendarSummary', None)
        """
        Retrieve the value for the "CalendarTimezone" output from this choreography execution. ((string) The calendar timezone parsed from the Google response.)
        """
        def get_CalendarTimezone(self):
            return self._output.get('CalendarTimezone', None)

class SearchCalendarsByNameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchCalendarsByNameResultSet(response, path)
