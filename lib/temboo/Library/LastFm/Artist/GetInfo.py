
###############################################################################
#
# GetInfo
# Retrieves the metadata for an artist including biographical data.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetInfo(Choreography):

    """
    Create a new instance of the GetInfo Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/Artist/GetInfo')


    def new_input_set(self):
        return GetInfoInputSet()

    def _make_result_set(self, result, path):
        return GetInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetInfoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetInfo
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetInfoInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Artist input for this choreography. ((conditional, string) The artist name. Required unless providing MbID.)
        """
        def set_Artist(self, value):
            InputSet._set_input(self, 'Artist', value)

        """
        Set the value of the AutoCorrect input for this choreography. ((optional, boolean) Transform misspelled artist names into correct artist names. The corrected artist name will be returned in the response. Defaults to 0.)
        """
        def set_AutoCorrect(self, value):
            InputSet._set_input(self, 'AutoCorrect', value)

        """
        Set the value of the Language input for this choreography. ((optional, string) The language to return the biography in, expressed as an ISO 639 alpha-2 code.)
        """
        def set_Language(self, value):
            InputSet._set_input(self, 'Language', value)

        """
        Set the value of the MbID input for this choreography. ((conditional, string) The musicbrainz id for the artist. Required unless providing Artist.)
        """
        def set_MbID(self, value):
            InputSet._set_input(self, 'MbID', value)

        """
        Set the value of the Username input for this choreography. ((optional, string) The username for the context of the request. If supplied, the user's playcount for this artist is included in the response.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GetInfo choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetInfoResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetInfoResultSet(response, path)
