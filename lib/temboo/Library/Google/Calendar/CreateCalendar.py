
###############################################################################
#
# CreateCalendar
# Create a new secondary calendar.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateCalendar(Choreography):

    """
    Create a new instance of the CreateCalendar Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Calendar/CreateCalendar')


    def new_input_set(self):
        return CreateCalendarInputSet()

    def _make_result_set(self, result, path):
        return CreateCalendarResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateCalendarChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateCalendar
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateCalendarInputSet(InputSet):
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
        Set the value of the Timezone input for this choreography. ((optional, string) The timezone for the new calendar, such as "America/Los_Angeles". Defaults to UTC if left blank.)
        """
        def set_Timezone(self, value):
            InputSet._set_input(self, 'Timezone', value)

        """
        Set the value of the Title input for this choreography. ((required, string) The name for the new calendar.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)


"""
A ResultSet with methods tailored to the values returned by the CreateCalendar choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateCalendarResultSet(ResultSet):
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

class CreateCalendarChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateCalendarResultSet(response, path)
