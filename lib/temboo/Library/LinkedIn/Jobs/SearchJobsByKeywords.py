
###############################################################################
#
# SearchJobsByKeywords
# Retrieve jobs matching the specified keyword(s).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchJobsByKeywords(Choreography):

    """
    Create a new instance of the SearchJobsByKeywords Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LinkedIn/Jobs/SearchJobsByKeywords')


    def new_input_set(self):
        return SearchJobsByKeywordsInputSet()

    def _make_result_set(self, result, path):
        return SearchJobsByKeywordsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchJobsByKeywordsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchJobsByKeywords
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchJobsByKeywordsInputSet(InputSet):
        """
        Set the value of the Count input for this choreography. ((optional, integer) Specify the number of jobs to be returned.  Default is 10.  The maximum is 20.)
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the Keywords input for this choreography. ((required, string) Limit search by specified keyword(s).)
        """
        def set_Keywords(self, value):
            InputSet._set_input(self, 'Keywords', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The Oauth Consumer Key provided by LinkedIn after registering your application.)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by LinkedIn after registering your application.)
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
        Set the value of the Sort input for this choreography. ((optional, string) Specify the ordering of results. Enter R (for relationship from job to member); DA (dated posted in ascending order); DO (job posted in descending order).)
        """
        def set_Sort(self, value):
            InputSet._set_input(self, 'Sort', value)


"""
A ResultSet with methods tailored to the values returned by the SearchJobsByKeywords choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchJobsByKeywordsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from LinkedIn in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchJobsByKeywordsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchJobsByKeywordsResultSet(response, path)
