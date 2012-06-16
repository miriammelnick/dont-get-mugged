
###############################################################################
#
# StatusesShow
# Retrieves a single status with a given id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class StatusesShow(Choreography):

    """
    Create a new instance of the StatusesShow Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Tweets/StatusesShow')


    def new_input_set(self):
        return StatusesShowInputSet()

    def _make_result_set(self, result, path):
        return StatusesShowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return StatusesShowChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the StatusesShow
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class StatusesShowInputSet(InputSet):
        """
        Set the value of the ID input for this choreography. ((required, integer) The numerical ID of the desired status.)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)

        """
        Set the value of the IncludeEntities input for this choreography. ((optional, boolean) When set to either true, t or 1, each tweet will include a node called "entities,". This node offers a variety of metadata about the tweet.)
        """
        def set_IncludeEntities(self, value):
            InputSet._set_input(self, 'IncludeEntities', value)

        """
        Set the value of the TrimUser input for this choreography. ((optional, boolean) When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID.)
        """
        def set_TrimUser(self, value):
            InputSet._set_input(self, 'TrimUser', value)


"""
A ResultSet with methods tailored to the values returned by the StatusesShow choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class StatusesShowResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Twitter in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class StatusesShowChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return StatusesShowResultSet(response, path)
