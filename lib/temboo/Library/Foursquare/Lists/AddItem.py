
###############################################################################
#
# AddItem
# Allows a user to add an item to a list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddItem(Choreography):

    """
    Create a new instance of the AddItem Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Lists/AddItem')


    def new_input_set(self):
        return AddItemInputSet()

    def _make_result_set(self, result, path):
        return AddItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddItemChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddItem
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddItemInputSet(InputSet):
        """
        Set the value of the ItemID input for this choreography. ((conditional, string) The id of an item on a list that you wish to copy to the target list. Used in conjuction with ListID. Note that one of the following must be specified: VenueID, TipID, ItemListID, or ItemID.)
        """
        def set_ItemID(self, value):
            InputSet._set_input(self, 'ItemID', value)

        """
        Set the value of the ItemListID input for this choreography. ((conditional, string) The ID of a list that contains an item that you wish to copy to the new list. Used in conjuction with ItemID. Note that one of the following must be specified: VenueID, TipID, ItemListID, or ItemID.)
        """
        def set_ItemListID(self, value):
            InputSet._set_input(self, 'ItemListID', value)

        """
        Set the value of the ListID input for this choreography. ((required, string) The ID of the list that  you are adding an item to. This can be a user-created list id or one of tips, todos, or dones.)
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
        Set the value of the Text input for this choreography. ((optional, string) If the target is a user-created list, this will create a public tip on the venue. If the target is todos, the text will be a private note that is only visible to the author.)
        """
        def set_Text(self, value):
            InputSet._set_input(self, 'Text', value)

        """
        Set the value of the TipID input for this choreography. ((conditional, string) The id of a tip to add to the list. Cannot be used in conjunction with the Text and URL inputs. Note that one of the following must be specified: VenueID, TipID, ItemListID, or ItemID.)
        """
        def set_TipID(self, value):
            InputSet._set_input(self, 'TipID', value)

        """
        Set the value of the URL input for this choreography. ((optional, string) If adding a new tip using the Text input, this can associate a url with the tip.)
        """
        def set_URL(self, value):
            InputSet._set_input(self, 'URL', value)

        """
        Set the value of the VenueID input for this choreography. ((conditional, string) The id of a venue to add to the list. Note that one of the following must be specified: VenueID, TipID, ItemListID, or ItemID.)
        """
        def set_VenueID(self, value):
            InputSet._set_input(self, 'VenueID', value)


"""
A ResultSet with methods tailored to the values returned by the AddItem choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddItemResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AddItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddItemResultSet(response, path)
