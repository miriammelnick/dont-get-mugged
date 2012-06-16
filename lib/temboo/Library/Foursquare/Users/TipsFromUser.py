
###############################################################################
#
# TipsFromUser
# Returns tips from a user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TipsFromUser(Choreography):

    """
    Create a new instance of the TipsFromUser Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Users/TipsFromUser')


    def new_input_set(self):
        return TipsFromUserInputSet()

    def _make_result_set(self, result, path):
        return TipsFromUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TipsFromUserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TipsFromUser
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TipsFromUserInputSet(InputSet):
        """
        Set the value of the Latitude input for this choreography. ((optional, decimal) The latitude point of the user's location.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Number of results to return, up to 500.)
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
        Set the value of the Offset input for this choreography. ((optional, integer) Used to page through results.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Sort input for this choreography. ((optional, string) Enter: recent, nearby, or popular. NEARBY requires geolat and geolong to be provided.)
        """
        def set_Sort(self, value):
            InputSet._set_input(self, 'Sort', value)

        """
        Set the value of the UserID input for this choreography. ((optional, string) Identity of the user to get tips for. Defaults to "self" to get lists of the acting user.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the TipsFromUser choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TipsFromUserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TipsFromUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TipsFromUserResultSet(response, path)
