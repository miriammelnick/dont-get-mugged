
###############################################################################
#
# SearchEvents
# Allows you to search for events using a variety of search parameters.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchEvents(Choreography):

    """
    Create a new instance of the SearchEvents Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Calendar/SearchEvents')


    def new_input_set(self):
        return SearchEventsInputSet()

    def _make_result_set(self, result, path):
        return SearchEventsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchEventsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchEvents
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchEventsInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the CalendarID input for this choreography. ((required, string) The unique ID for the calendar with the events to retrieve.)
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
        Set the value of the LastModified input for this choreography. ((optional, date) An event's last modification time (as a RFC 3339 timestamp) to filter by.)
        """
        def set_LastModified(self, value):
            InputSet._set_input(self, 'LastModified', value)

        """
        Set the value of the MaxAttendees input for this choreography. ((optional, integer) The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned.)
        """
        def set_MaxAttendees(self, value):
            InputSet._set_input(self, 'MaxAttendees', value)

        """
        Set the value of the MaxResults input for this choreography. ((optional, integer) The maximum number of events to return on one result page.)
        """
        def set_MaxResults(self, value):
            InputSet._set_input(self, 'MaxResults', value)

        """
        Set the value of the MaxTime input for this choreography. ((optional, date) The max start time to filter by (formatted like 2012-05-22T00:47:43.000Z).)
        """
        def set_MaxTime(self, value):
            InputSet._set_input(self, 'MaxTime', value)

        """
        Set the value of the MinTime input for this choreography. ((optional, date) The minimum start time to filter by (formatted like 2012-05-22T00:47:43.000Z).)
        """
        def set_MinTime(self, value):
            InputSet._set_input(self, 'MinTime', value)

        """
        Set the value of the OrderBy input for this choreography. ((optional, string) The order of the events returned in the result. Accepted values are: "startTime" (ordered by start date/time. Must set SingleEvents to 1 to use this) or "updated" (ordered by modification date/time).)
        """
        def set_OrderBy(self, value):
            InputSet._set_input(self, 'OrderBy', value)

        """
        Set the value of the PageToken input for this choreography. ((optional, integer) Indicates which result page to return. Used for paging through results.)
        """
        def set_PageToken(self, value):
            InputSet._set_input(self, 'PageToken', value)

        """
        Set the value of the Query input for this choreography. ((optional, string) A keyword search to find events.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

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
        Set the value of the ShowDeleted input for this choreography. ((optional, boolean) Whether to include deleted events. Set to 1 (true) to include deleted events. Defaults to 0 (false).)
        """
        def set_ShowDeleted(self, value):
            InputSet._set_input(self, 'ShowDeleted', value)

        """
        Set the value of the ShowHiddenInvitations input for this choreography. ((optional, boolean) Whether to include hidden invitations in the result. Set to 1 (true) to enable. The default is 0 (false). )
        """
        def set_ShowHiddenInvitations(self, value):
            InputSet._set_input(self, 'ShowHiddenInvitations', value)

        """
        Set the value of the SingleEvent input for this choreography. ((optional, boolean) Whether to expand recurring events into instances and only return single one-off events and instances of recurring events. Defaults to 0 (false). )
        """
        def set_SingleEvent(self, value):
            InputSet._set_input(self, 'SingleEvent', value)

        """
        Set the value of the Timezone input for this choreography. ((optional, string) The time zone used in the response (i.e. America/Los_Angeles). The default is the time zone of the calendar. )
        """
        def set_Timezone(self, value):
            InputSet._set_input(self, 'Timezone', value)


"""
A ResultSet with methods tailored to the values returned by the SearchEvents choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchEventsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Google. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "AccessToken" output from this choreography execution. ((required, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def get_AccessToken(self):
            return self._output.get('AccessToken', None)

class SearchEventsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchEventsResultSet(response, path)
