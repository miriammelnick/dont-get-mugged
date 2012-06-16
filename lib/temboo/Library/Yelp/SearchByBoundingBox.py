
###############################################################################
#
# SearchByBoundingBox
# Retrieve businesses in a geograpic bounding box.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchByBoundingBox(Choreography):

    """
    Create a new instance of the SearchByBoundingBox Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Yelp/SearchByBoundingBox')


    def new_input_set(self):
        return SearchByBoundingBoxInputSet()

    def _make_result_set(self, result, path):
        return SearchByBoundingBoxResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByBoundingBoxChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchByBoundingBox
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchByBoundingBoxInputSet(InputSet):
        """
        Set the value of the BusinessType input for this choreography. ((optional, string) A term to narrow the search, such as "comic books" or "restaurants". Leave blank to search for all business types.)
        """
        def set_BusinessType(self, value):
            InputSet._set_input(self, 'BusinessType', value)

        """
        Set the value of the NortheastLatitude input for this choreography. ((required, decimal) The northeastern latitude of the bounding box to search, such as "37.788022".)
        """
        def set_NortheastLatitude(self, value):
            InputSet._set_input(self, 'NortheastLatitude', value)

        """
        Set the value of the NortheastLongitude input for this choreography. ((required, decimal) The northeastern longitude of the bounding box to search, such as "-122.399797".)
        """
        def set_NortheastLongitude(self, value):
            InputSet._set_input(self, 'NortheastLongitude', value)

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
        Set the value of the SouthwestLatitude input for this choreography. ((required, decimal) The southwestern latitude of the bounding box to search, such as "37.900000".)
        """
        def set_SouthwestLatitude(self, value):
            InputSet._set_input(self, 'SouthwestLatitude', value)

        """
        Set the value of the SouthwestLongitude input for this choreography. ((required, decimal) The southwestern longitude of the bounding box to search, such as "-122.500000".)
        """
        def set_SouthwestLongitude(self, value):
            InputSet._set_input(self, 'SouthwestLongitude', value)


"""
A ResultSet with methods tailored to the values returned by the SearchByBoundingBox choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchByBoundingBoxResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Yelp. Corresponds to the input value for ResponseFormat (defaults to JSON).)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchByBoundingBoxChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByBoundingBoxResultSet(response, path)
