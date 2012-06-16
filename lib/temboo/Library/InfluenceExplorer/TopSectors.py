
###############################################################################
#
# TopSectors
# Returns the contribution amounts that each sector gave to the politician.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TopSectors(Choreography):

    """
    Create a new instance of the TopSectors Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/InfluenceExplorer/TopSectors')


    def new_input_set(self):
        return TopSectorsInputSet()

    def _make_result_set(self, result, path):
        return TopSectorsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TopSectorsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TopSectors
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TopSectorsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API key provided by Sunlight Data Services.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the EntityID input for this choreography. ((required, string) The ID for the Entity that you want to return information for. This ID can be retrieved by running the SearchByName Choreo.)
        """
        def set_EntityID(self, value):
            InputSet._set_input(self, 'EntityID', value)


"""
A ResultSet with methods tailored to the values returned by the TopSectors choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TopSectorsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Influence Explorer.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TopSectorsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TopSectorsResultSet(response, path)
