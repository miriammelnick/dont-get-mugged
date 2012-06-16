
###############################################################################
#
# Query
# Executes a query against a Salesforce object and returns data that matches the specified criteria.
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
        Choreography.__init__(self, temboo_session, '/Library/Salesforce/Query')


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
        Set the value of the Password input for this choreography. ((required, string) Your Salesforce password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Query input for this choreography. ((required, string) The query to submit to Salesforce. This should be SOQL which differs from standard SQL in some cases (select FirstName, LastName from Lead limit 1).)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the SecurityToken input for this choreography. ((required, string) Your Salesforce security token for making API calls.)
        """
        def set_SecurityToken(self, value):
            InputSet._set_input(self, 'SecurityToken', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Salesforce username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the Query choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class QueryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from the Salesforce query)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class QueryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return QueryResultSet(response, path)
