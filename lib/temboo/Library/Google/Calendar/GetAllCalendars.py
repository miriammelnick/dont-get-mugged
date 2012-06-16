
###############################################################################
#
# GetAllCalendars
# Retrieve data for all calendars.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetAllCalendars(Choreography):

    """
    Create a new instance of the GetAllCalendars Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Calendar/GetAllCalendars')


    def new_input_set(self):
        return GetAllCalendarsInputSet()

    def _make_result_set(self, result, path):
        return GetAllCalendarsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAllCalendarsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetAllCalendars
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetAllCalendarsInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

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
        Set the value of the Count input for this choreography. ((optional, integer) The maximum number of calendars to return. The default is 15.)
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the Fields input for this choreography. ((optional, string) The calendar fields to return. Accepted values are "etag", "items", "kind", and "nextPageToken". All calendar items are returned by default.)
        """
        def set_Fields(self, value):
            InputSet._set_input(self, 'Fields', value)

        """
        Set the value of the Hidden input for this choreography. ((optional, boolean) Enter "1" to return hidden calendars in the results, or "0" (the default) to not return them.)
        """
        def set_Hidden(self, value):
            InputSet._set_input(self, 'Hidden', value)

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
A ResultSet with methods tailored to the values returned by the GetAllCalendars choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetAllCalendarsResultSet(ResultSet):
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

class GetAllCalendarsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAllCalendarsResultSet(response, path)
