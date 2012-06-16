
###############################################################################
#
# PublicTimeline
# Retrieves the 20 most recent statuses, including retweets if they exist, from non-protected users.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PublicTimeline(Choreography):

    """
    Create a new instance of the PublicTimeline Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Timelines/PublicTimeline')


    def new_input_set(self):
        return PublicTimelineInputSet()

    def _make_result_set(self, result, path):
        return PublicTimelineResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PublicTimelineChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PublicTimeline
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PublicTimelineInputSet(InputSet):
        """
        Set the value of the IncludeEntities input for this choreography. ((optional, boolean) An advanced option for returning more verbose metadata. When set to either true, t or 1, each tweet will include a node called "entities".)
        """
        def set_IncludeEntities(self, value):
            InputSet._set_input(self, 'IncludeEntities', value)

        """
        Set the value of the TrimUser input for this choreography. ((optional, boolean) When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Defaults to false.)
        """
        def set_TrimUser(self, value):
            InputSet._set_input(self, 'TrimUser', value)


"""
A ResultSet with methods tailored to the values returned by the PublicTimeline choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PublicTimelineResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Twitter in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PublicTimelineChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PublicTimelineResultSet(response, path)
