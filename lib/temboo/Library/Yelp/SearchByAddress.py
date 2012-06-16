
###############################################################################
#
# SearchByAddress
# Retrieve businesses within a specific range of a specified address.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchByAddress(Choreography):

    """
    Create a new instance of the SearchByAddress Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Yelp/SearchByAddress')


    def new_input_set(self):
        return SearchByAddressInputSet()

    def _make_result_set(self, result, path):
        return SearchByAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByAddressChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchByAddress
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchByAddressInputSet(InputSet):
        """
        Set the value of the Address input for this choreography. ((required, string) The street address of the business to search for.)
        """
        def set_Address(self, value):
            InputSet._set_input(self, 'Address', value)

        """
        Set the value of the BusinessType input for this choreography. ((optional, string) A term to narrow the search, such as "shoes" or "restaurants". Leave blank to search for all business types.)
        """
        def set_BusinessType(self, value):
            InputSet._set_input(self, 'BusinessType', value)

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
        Set the value of the Range input for this choreography. ((required, integer) Narrow or expand a search by specifying a range in either feet, meters, miles, or kilometers, depending on the value of the Units input. The default is 200 feet, and the maximum is 2,500 square miles.)
        """
        def set_Range(self, value):
            InputSet._set_input(self, 'Range', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format of the response from Yelp, either XML or JSON (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Units input for this choreography. ((required, string) Specify "feet" (the default), "meters", "miles", or "kilometers". Units apply to the Range input value.)
        """
        def set_Units(self, value):
            InputSet._set_input(self, 'Units', value)


"""
A ResultSet with methods tailored to the values returned by the SearchByAddress choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchByAddressResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Yelp. Corresponds to the input value for ResponseFormat (defaults to JSON).)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchByAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByAddressResultSet(response, path)
