
###############################################################################
#
# FilterPlacesByCategories
# Filter queries by category.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FilterPlacesByCategories(Choreography):

    """
    Create a new instance of the FilterPlacesByCategories Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Factual/FilterPlacesByCategories')


    def new_input_set(self):
        return FilterPlacesByCategoriesInputSet()

    def _make_result_set(self, result, path):
        return FilterPlacesByCategoriesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FilterPlacesByCategoriesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FilterPlacesByCategories
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FilterPlacesByCategoriesInputSet(InputSet):
        """
        Set the value of the Category input for this choreography. ((required, string) Enter a Factual category to narrow the search results.)
        """
        def set_Category(self, value):
            InputSet._set_input(self, 'Category', value)

        """
        Set the value of the City input for this choreography. ((required, string) Enter a city to narrow results to.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The Oauth Consumer Key provided by Factual after registering your application.)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by Factual after registering your application.)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the Query input for this choreography. ((optional, string) A search string (i.e. Starbucks))
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)


"""
A ResultSet with methods tailored to the values returned by the FilterPlacesByCategories choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FilterPlacesByCategoriesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Factual.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FilterPlacesByCategoriesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FilterPlacesByCategoriesResultSet(response, path)
