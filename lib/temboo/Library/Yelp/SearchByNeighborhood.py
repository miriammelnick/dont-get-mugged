
###############################################################################
#
# SearchByNeighborhood
# Retrieve businesses by neighborhood.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchByNeighborhood(Choreography):

    """
    Create a new instance of the SearchByNeighborhood Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Yelp/SearchByNeighborhood')


    def new_input_set(self):
        return SearchByNeighborhoodInputSet()

    def _make_result_set(self, result, path):
        return SearchByNeighborhoodResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByNeighborhoodChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchByNeighborhood
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchByNeighborhoodInputSet(InputSet):
        """
        Set the value of the BusinessType input for this choreography. ((optional, string) A term to narrow the search, such as "wine" or "restaurants". Leave blank to search for all business types.)
        """
        def set_BusinessType(self, value):
            InputSet._set_input(self, 'BusinessType', value)

        """
        Set the value of the Count input for this choreography. ((optional, integer) The number of businesses to return. The default is 15.)
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the Neighborhood input for this choreography. ((required, string) The neighborhood in which to search for businesses. See the Yelp API documentation for a list of supported neighborhoods.)
        """
        def set_Neighborhood(self, value):
            InputSet._set_input(self, 'Neighborhood', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The OAuth Consumer Key provided by Yelp after registering your application.)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by Yelp after registering your application.)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((required, string) The OAuth token secret provided by Yelp when you registered your application.)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The OAuth access token provided by Yelp when you registered your application.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format of the response from Yelp, either XML or JSON (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the SearchByNeighborhood choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchByNeighborhoodResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Yelp. Corresponds to the input value for ResponseFormat (defaults to JSON).)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchByNeighborhoodChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByNeighborhoodResultSet(response, path)
