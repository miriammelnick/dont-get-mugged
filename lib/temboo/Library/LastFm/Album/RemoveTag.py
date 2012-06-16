
###############################################################################
#
# RemoveTag
# Removes a user's tag from a specified album.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RemoveTag(Choreography):

    """
    Create a new instance of the RemoveTag Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/Album/RemoveTag')


    def new_input_set(self):
        return RemoveTagInputSet()

    def _make_result_set(self, result, path):
        return RemoveTagResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RemoveTagChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RemoveTag
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RemoveTagInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((string) Your Last.fm API Secret.)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the Album input for this choreography. ((string) The album name.)
        """
        def set_Album(self, value):
            InputSet._set_input(self, 'Album', value)

        """
        Set the value of the Artist input for this choreography. ((string) The artist name.)
        """
        def set_Artist(self, value):
            InputSet._set_input(self, 'Artist', value)

        """
        Set the value of the SessionKey input for this choreography. ((string) The session key retrieved in the last step of the authorization process.)
        """
        def set_SessionKey(self, value):
            InputSet._set_input(self, 'SessionKey', value)

        """
        Set the value of the Tag input for this choreography. ((string) A single user tag to remove from this album.)
        """
        def set_Tag(self, value):
            InputSet._set_input(self, 'Tag', value)


"""
A ResultSet with methods tailored to the values returned by the RemoveTag choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RemoveTagResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RemoveTagChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RemoveTagResultSet(response, path)
