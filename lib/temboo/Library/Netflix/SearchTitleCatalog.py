
###############################################################################
#
# SearchTitleCatalog
# Searches for a title in the instant-watch title catalog.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchTitleCatalog(Choreography):

    """
    Create a new instance of the SearchTitleCatalog Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Netflix/SearchTitleCatalog')


    def new_input_set(self):
        return SearchTitleCatalogInputSet()

    def _make_result_set(self, result, path):
        return SearchTitleCatalogResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchTitleCatalogChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchTitleCatalog
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchTitleCatalogInputSet(InputSet):
        """
        Set the value of the MaxResults input for this choreography. ((optional, integer) Set this to the maximum number of results to return. This number cannot be greater than 500. If you do not specify max_results, the default value is 25)
        """
        def set_MaxResults(self, value):
            InputSet._set_input(self, 'MaxResults', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The Oauth Consumer Key provided by Neflix after registering your application.)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by Netflix after registering your application.)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((required, string) The Oauth Token Secret retrieved during the Oauth process.)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The Oauth Token retrieved during the Oauth process.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the StartIndex input for this choreography. ((optional, integer) The offset number of the results from the query.)
        """
        def set_StartIndex(self, value):
            InputSet._set_input(self, 'StartIndex', value)

        """
        Set the value of the Term input for this choreography. ((required, string) Enter a word or phrase to search for in the instant-watch catalog. The Netflix API searches for matching titles and synopses in the catalog.)
        """
        def set_Term(self, value):
            InputSet._set_input(self, 'Term', value)


"""
A ResultSet with methods tailored to the values returned by the SearchTitleCatalog choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchTitleCatalogResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Netflix.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchTitleCatalogChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchTitleCatalogResultSet(response, path)
