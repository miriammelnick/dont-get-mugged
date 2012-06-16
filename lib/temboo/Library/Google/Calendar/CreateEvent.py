
###############################################################################
#
# CreateEvent
# Create a new event in a specified calendar.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateEvent(Choreography):

    """
    Create a new instance of the CreateEvent Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Calendar/CreateEvent')


    def new_input_set(self):
        return CreateEventInputSet()

    def _make_result_set(self, result, path):
        return CreateEventResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateEventChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateEvent
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateEventInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the CalendarID input for this choreography. ((required, string) The ID for the calendar in which to add the event.)
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
        Set the value of the EndDate input for this choreography. ((required, string) The end date of the event, in the format "2012-04-10".)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the EndTime input for this choreography. ((required, string) The end time for the event, in the format "10:30:00".)
        """
        def set_EndTime(self, value):
            InputSet._set_input(self, 'EndTime', value)

        """
        Set the value of the EventDescription input for this choreography. ((optional, string) A short description of the event.)
        """
        def set_EventDescription(self, value):
            InputSet._set_input(self, 'EventDescription', value)

        """
        Set the value of the EventLocation input for this choreography. ((optional, string) The location for the new event.)
        """
        def set_EventLocation(self, value):
            InputSet._set_input(self, 'EventLocation', value)

        """
        Set the value of the EventTitle input for this choreography. ((required, string) The title for the new event.)
        """
        def set_EventTitle(self, value):
            InputSet._set_input(self, 'EventTitle', value)

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
        Set the value of the StartDate input for this choreography. ((required, string) The start date of the event, in the format "2012-11-03".)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the StartTime input for this choreography. ((required, string) The start time for the event, in the format "10:00:00".)
        """
        def set_StartTime(self, value):
            InputSet._set_input(self, 'StartTime', value)


"""
A ResultSet with methods tailored to the values returned by the CreateEvent choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateEventResultSet(ResultSet):
        """
        Retrieve the value for the "CreateEvent" output from this choreography execution. (The request template with appropriate inputs passed.)
        """
        def get_CreateEvent(self):
            return self._output.get('CreateEvent', None)
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Google. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "TimezoneSetting" output from this choreography execution. ((string) The timezone setting retrieved from the specified calendar.)
        """
        def get_TimezoneSetting(self):
            return self._output.get('TimezoneSetting', None)
        """
        Retrieve the value for the "AccessToken" output from this choreography execution. ((required, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def get_AccessToken(self):
            return self._output.get('AccessToken', None)

class CreateEventChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateEventResultSet(response, path)
