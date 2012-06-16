
###############################################################################
#
# SearchNearbyTips
# Get a list of tips near the specified area.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchNearbyTips(Choreography):

    """
    Create a new instance of the SearchNearbyTips Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Tips/SearchNearbyTips')


    def new_input_set(self):
        return SearchNearbyTipsInputSet()

    def _make_result_set(self, result, path):
        return SearchNearbyTipsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchNearbyTipsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchNearbyTips
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchNearbyTipsInputSet(InputSet):
        """
        Set the value of the Filter input for this choreography. ((optional, string) Filter results.  If set to 'friends', the choreo returns tips from friends.)
        """
        def set_Filter(self, value):
            InputSet._set_input(self, 'Filter', value)

        """
        Set the value of the Latitude input for this choreography. ((required, decimal) The latitude point of the user's location.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Number of results to be returned by the search, up to 500.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) The longitude point of the user's location.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) Your Foursquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) Use to page through the list of results.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the Query input for this choreography. ((optional, string) Only find tips matching the given term. Cannot be used in conjunction with 'friends' filter.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the SearchNearbyTips choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchNearbyTipsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchNearbyTipsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchNearbyTipsResultSet(response, path)
