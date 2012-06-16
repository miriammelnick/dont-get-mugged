
###############################################################################
#
# GetPersonalTags
# Retrieves a user's personal tags.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetPersonalTags(Choreography):

    """
    Create a new instance of the GetPersonalTags Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetPersonalTags')


    def new_input_set(self):
        return GetPersonalTagsInputSet()

    def _make_result_set(self, result, path):
        return GetPersonalTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPersonalTagsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetPersonalTags
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetPersonalTagsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of results to fetch per page. Defaults to 50.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page number to fetch. Defaults to 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the Tag input for this choreography. ((string) The tag you're interested in.)
        """
        def set_Tag(self, value):
            InputSet._set_input(self, 'Tag', value)

        """
        Set the value of the TaggingType input for this choreography. ((string) The type of items which have been tagged. Valid values are: artist, album, track.)
        """
        def set_TaggingType(self, value):
            InputSet._set_input(self, 'TaggingType', value)

        """
        Set the value of the User input for this choreography. ((string) The user who performed the taggings.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the GetPersonalTags choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetPersonalTagsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetPersonalTagsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPersonalTagsResultSet(response, path)
