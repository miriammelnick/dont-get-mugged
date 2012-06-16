
###############################################################################
#
# CommentDelete
# Deletes a specified comment.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CommentDelete(Choreography):

    """
    Create a new instance of the CommentDelete Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/CommentDelete')


    def new_input_set(self):
        return CommentDeleteInputSet()

    def _make_result_set(self, result, path):
        return CommentDeleteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CommentDeleteChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CommentDelete
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CommentDeleteInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the CommentID input for this choreography. ((required, string) The id of the comment to delete)
        """
        def set_CommentID(self, value):
            InputSet._set_input(self, 'CommentID', value)


"""
A ResultSet with methods tailored to the values returned by the CommentDelete choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CommentDeleteResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((boolean) The response from Facebook. Returns "true" on success.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CommentDeleteChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CommentDeleteResultSet(response, path)
