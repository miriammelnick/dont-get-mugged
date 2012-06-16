
###############################################################################
#
# RecentCheckins
# Returns a list of recent friends' checkins.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RecentCheckins(Choreography):

    """
    Create a new instance of the RecentCheckins Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Checkins/RecentCheckins')


    def new_input_set(self):
        return RecentCheckinsInputSet()

    def _make_result_set(self, result, path):
        return RecentCheckinsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RecentCheckinsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RecentCheckins
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RecentCheckinsInputSet(InputSet):
        """
        Set the value of the AfterTimeStamp input for this choreography. ((optional, integer) Seconds after which to look for checkins, e.g. for looking for new checkins since the last fetch.)
        """
        def set_AfterTimeStamp(self, value):
            InputSet._set_input(self, 'AfterTimeStamp', value)

        """
        Set the value of the Latitude input for this choreography. ((optional, decimal) The latitude point of the user's location.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Number of results to return, up to 100.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Longitude input for this choreography. ((optional, decimal) The longitude point of the user's location.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The FourSquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the RecentCheckins choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RecentCheckinsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RecentCheckinsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RecentCheckinsResultSet(response, path)
