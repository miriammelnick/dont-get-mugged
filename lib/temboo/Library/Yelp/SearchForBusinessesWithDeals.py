
###############################################################################
#
# SearchForBusinessesWithDeals
# Only returns information for businesses with deals.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchForBusinessesWithDeals(Choreography):

    """
    Create a new instance of the SearchForBusinessesWithDeals Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Yelp/SearchForBusinessesWithDeals')


    def new_input_set(self):
        return SearchForBusinessesWithDealsInputSet()

    def _make_result_set(self, result, path):
        return SearchForBusinessesWithDealsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchForBusinessesWithDealsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchForBusinessesWithDeals
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchForBusinessesWithDealsInputSet(InputSet):
        """
        Set the value of the Accuracy input for this choreography. ((optional, integer) Narrow or widen the search range in relation to the coordinates, such as "2" for state or "8" for street address.)
        """
        def set_Accuracy(self, value):
            InputSet._set_input(self, 'Accuracy', value)

        """
        Set the value of the BusinessType input for this choreography. ((optional, string) A term to narrow the search, such as "comic books" or "restaurants". Leave blank to search for all business types.)
        """
        def set_BusinessType(self, value):
            InputSet._set_input(self, 'BusinessType', value)

        """
        Set the value of the Category input for this choreography. ((optional, string) Yelp categories to search in, separated by commas but no spaces, such as "hiking,climbing". See the Yelp API docimentation for a list of categories.)
        """
        def set_Category(self, value):
            InputSet._set_input(self, 'Category', value)

        """
        Set the value of the Latitude input for this choreography. ((conditional, decimal) The latitude to search near, such as "37.788022". Searching with either Location or Coordinates is required.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Location input for this choreography. ((conditional, string)  An address, neighborhood, city, state, or ZIP code in which to search for the category. Searching with either Location or Coordinates is required.)
        """
        def set_Location(self, value):
            InputSet._set_input(self, 'Location', value)

        """
        Set the value of the Longitude input for this choreography. ((conditional, decimal) The longitude to search near, such as "-122.399797". Searching with either Location or Coordinates is required.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

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
A ResultSet with methods tailored to the values returned by the SearchForBusinessesWithDeals choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchForBusinessesWithDealsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Yelp. Corresponds to the input value for ResponseFormat (defaults to JSON).)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchForBusinessesWithDealsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchForBusinessesWithDealsResultSet(response, path)
