
###############################################################################
#
# DeleteItem
# Allows a user to delete an item from a list.

#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteItem(Choreography):

    """
    Create a new instance of the DeleteItem Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Lists/DeleteItem')


    def new_input_set(self):
        return DeleteItemInputSet()

    def _make_result_set(self, result, path):
        return DeleteItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteItemChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteItem
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteItemInputSet(InputSet):
        """
        Set the value of the ItemID input for this choreography. ((required, string) The id of the item to delete.)
        """
        def set_ItemID(self, value):
            InputSet._set_input(self, 'ItemID', value)

        """
        Set the value of the ListID input for this choreography. ((required, string) This can be a user-created list id or one of tips, todos, or dones.)
        """
        def set_ListID(self, value):
            InputSet._set_input(self, 'ListID', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The FourSquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteItem choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteItemResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteItemResultSet(response, path)
