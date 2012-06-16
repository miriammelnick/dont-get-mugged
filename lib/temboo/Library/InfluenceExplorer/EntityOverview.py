
###############################################################################
#
# EntityOverview
# Returns general information about a particular politician, individual, or organization with a given entity id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class EntityOverview(Choreography):

    """
    Create a new instance of the EntityOverview Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/InfluenceExplorer/EntityOverview')


    def new_input_set(self):
        return EntityOverviewInputSet()

    def _make_result_set(self, result, path):
        return EntityOverviewResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EntityOverviewChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the EntityOverview
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class EntityOverviewInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API key provided by Sunlight Data Services.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Cycle input for this choreography. ((optional, date) Specify a yyyy-formatted election cycle. Example: 2012, or 2008|2012 to limit results between 2008 and 2012.)
        """
        def set_Cycle(self, value):
            InputSet._set_input(self, 'Cycle', value)

        """
        Set the value of the EntityID input for this choreography. ((required, string) The ID for the Entity that you want to return information for. This ID can be retrieved by running the SearchByName Choreo.)
        """
        def set_EntityID(self, value):
            InputSet._set_input(self, 'EntityID', value)


"""
A ResultSet with methods tailored to the values returned by the EntityOverview choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class EntityOverviewResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Influence Explorer.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class EntityOverviewChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EntityOverviewResultSet(response, path)
