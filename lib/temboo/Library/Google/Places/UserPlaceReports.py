
###############################################################################
#
# UserPlaceReports
# Add a new Place to Google Places.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UserPlaceReports(Choreography):

    """
    Create a new instance of the UserPlaceReports Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Places/UserPlaceReports')


    def new_input_set(self):
        return UserPlaceReportsInputSet()

    def _make_result_set(self, result, path):
        return UserPlaceReportsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UserPlaceReportsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UserPlaceReports
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UserPlaceReportsInputSet(InputSet):
        """
        Set the value of the POSTForm input for this choreography. ((required, any) Enter the required POST parameter, reference in the body of this JSON form.)
        """
        def set_POSTForm(self, value):
            InputSet._set_input(self, 'POSTForm', value)

        """
        Set the value of the Key input for this choreography. ((required, string) Enter your Google API key.)
        """
        def set_Key(self, value):
            InputSet._set_input(self, 'Key', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Sensor input for this choreography. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        def set_Sensor(self, value):
            InputSet._set_input(self, 'Sensor', value)


"""
A ResultSet with methods tailored to the values returned by the UserPlaceReports choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UserPlaceReportsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UserPlaceReportsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UserPlaceReportsResultSet(response, path)
