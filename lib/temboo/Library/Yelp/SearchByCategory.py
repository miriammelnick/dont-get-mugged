
###############################################################################
#
# SearchByCategory
# Retrieve businesses in a specific location by business category.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchByCategory(Choreography):

    """
    Create a new instance of the SearchByCategory Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Yelp/SearchByCategory')


    def new_input_set(self):
        return SearchByCategoryInputSet()

    def _make_result_set(self, result, path):
        return SearchByCategoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByCategoryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchByCategory
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchByCategoryInputSet(InputSet):
        """
        Set the value of the Category input for this choreography. ((required, string) Yelp categories to search in, separated by commas but no spaces, such as "hiking,climbing". See the Yelp API docimentation for a list of categories.)
        """
        def set_Category(self, value):
            InputSet._set_input(self, 'Category', value)

        """
        Set the value of the Count input for this choreography. ((optional, integer) The number of businesses to return. The default is 15.)
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the Location input for this choreography. ((required, string) An address, neighborhood, city, state, or ZIP code in which to search for the category.)
        """
        def set_Location(self, value):
            InputSet._set_input(self, 'Location', value)

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
A ResultSet with methods tailored to the values returned by the SearchByCategory choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchByCategoryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Yelp. Corresponds to the input value for ResponseFormat (defaults to JSON).)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchByCategoryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByCategoryResultSet(response, path)
