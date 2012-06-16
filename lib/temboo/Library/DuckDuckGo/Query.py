
###############################################################################
#
# Query
# Access DuckDuckGo web search functionality.  
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
        Choreography.__init__(self, temboo_session, '/Library/DuckDuckGo/Query')


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
        Set the value of the Format input for this choreography. ((optional, string) Enter: xml, or json.  Default is set to xml.)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the NoHTML input for this choreography. ((optional, integer) Enter 1 to remove HTML from text. Set only if Format=json.)
        """
        def set_NoHTML(self, value):
            InputSet._set_input(self, 'NoHTML', value)

        """
        Set the value of the NoRedirect input for this choreography. ((optional, integer) Enter 1 to skip HTTP redirects.  This is useful for !bang commands. Set only if Format=json.)
        """
        def set_NoRedirect(self, value):
            InputSet._set_input(self, 'NoRedirect', value)

        """
        Set the value of the PrettyPrint input for this choreography. ((optional, integer) Enter 1 to pretty-print the JSON output.)
        """
        def set_PrettyPrint(self, value):
            InputSet._set_input(self, 'PrettyPrint', value)

        """
        Set the value of the Query input for this choreography. ((required, string) Enter a search query.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the SkipDisambiguation input for this choreography. ((optional, integer) Enter 1 to skip disambiguation. Set only if Format=json.)
        """
        def set_SkipDisambiguation(self, value):
            InputSet._set_input(self, 'SkipDisambiguation', value)


"""
A ResultSet with methods tailored to the values returned by the Query choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class QueryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from DuckDuckGo in XML or JSON format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class QueryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return QueryResultSet(response, path)
