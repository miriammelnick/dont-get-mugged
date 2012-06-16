
###############################################################################
#
# Query
# Retrieves tweets that match a specified query.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Query(Choreography):

    """
    Create a new instance of the Query Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Search/Query')


    def new_input_set(self):
        return QueryInputSet()

    def _make_result_set(self, result, path):
        return QueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return QueryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Query
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class QueryInputSet(InputSet):
        """
        Set the value of the Geocode input for this choreography. ((optional, string) Returns tweets by users located within a given radius of the given latitude/longitude. Should be specified in a string like "latitude,longitude,radius" (i.e. 37.781157,-122.398720,1mi).)
        """
        def set_Geocode(self, value):
            InputSet._set_input(self, 'Geocode', value)

        """
        Set the value of the IncludeEntities input for this choreography. ((optional, boolean) When set to either true, t or 1, each tweet will include a node called "entities". This node offers a variety of extra metadata about the tweet.)
        """
        def set_IncludeEntities(self, value):
            InputSet._set_input(self, 'IncludeEntities', value)

        """
        Set the value of the Language input for this choreography. ((optional, string) Restricts tweets to the given language, given by an ISO 639-1 code.)
        """
        def set_Language(self, value):
            InputSet._set_input(self, 'Language', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page number (starting at 1) to return, up to a max of roughly 1500 results. Used in conjunction with the ResultPerPage input.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the Query input for this choreography. ((required, string) A search string to use for the query.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the ResultType input for this choreography. ((optional, string) Specifies what type of search results you would prefer to receive. Valid values are: mixed, recent, or popular.)
        """
        def set_ResultType(self, value):
            InputSet._set_input(self, 'ResultType', value)

        """
        Set the value of the ResultsPerPage input for this choreography. ((optional, integer) The number of tweets to return per page, up to a max of 100.)
        """
        def set_ResultsPerPage(self, value):
            InputSet._set_input(self, 'ResultsPerPage', value)

        """
        Set the value of the ShowUser input for this choreography. ((optional, boolean) When true, prepends ":" to the beginning of the tweet. This is useful for readers that do not display Atom's author field.)
        """
        def set_ShowUser(self, value):
            InputSet._set_input(self, 'ShowUser', value)

        """
        Set the value of the SinceId input for this choreography. ((optional, integer) Returns results with an ID greater than (that is, more recent than) the specified ID.)
        """
        def set_SinceId(self, value):
            InputSet._set_input(self, 'SinceId', value)

        """
        Set the value of the Until input for this choreography. ((optional, date) Returns tweets generated before the given date. Date should be formatted as YYYY-MM-DD.)
        """
        def set_Until(self, value):
            InputSet._set_input(self, 'Until', value)


"""
A ResultSet with methods tailored to the values returned by the Query choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class QueryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) )
        """
        def get_Response(self):
            return self._output.get('Response', None)

class QueryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return QueryResultSet(response, path)
