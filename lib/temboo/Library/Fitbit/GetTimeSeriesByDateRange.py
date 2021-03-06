
###############################################################################
#
# GetTimeSeriesByDateRange
# Gets time series data for a given resource based on a date range you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTimeSeriesByDateRange(Choreography):

    """
    Create a new instance of the GetTimeSeriesByDateRange Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Fitbit/GetTimeSeriesByDateRange')


    def new_input_set(self):
        return GetTimeSeriesByDateRangeInputSet()

    def _make_result_set(self, result, path):
        return GetTimeSeriesByDateRangeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTimeSeriesByDateRangeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTimeSeriesByDateRange
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTimeSeriesByDateRangeInputSet(InputSet):
        """
        Set the value of the EndDate input for this choreography. ((date) The end date of the date range for the data you want to retrieve (in the format yyyy-MM-dd). You can also specify the value 'today'.)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the Format input for this choreography. ((optional, string) The format that you want the response to be in: xml or json. Defaults to xml.)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((string) The Oauth Consumer Key provided by Fitbit after registering your application)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((string) The Oauth Consumer Secret provided by Fitbit after registering your application)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((string) The Oauth Token Secret retrieved during the Oauth process)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((string) The Oauth Token retrieved during the Oauth process)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResourcePath input for this choreography. ((optional, string) The resource path that you want to access (for example: activities/log/distance). See Choreo documentation for a full list of resource paths.)
        """
        def set_ResourcePath(self, value):
            InputSet._set_input(self, 'ResourcePath', value)

        """
        Set the value of the StartDate input for this choreography. ((date) The start date of the date range for the data you want to retrieve (in the format yyyy-MM-dd). You can also specify the value 'today'.)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the UserId input for this choreography. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided. )
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the GetTimeSeriesByDateRange choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTimeSeriesByDateRangeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Fitbit in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTimeSeriesByDateRangeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTimeSeriesByDateRangeResultSet(response, path)
