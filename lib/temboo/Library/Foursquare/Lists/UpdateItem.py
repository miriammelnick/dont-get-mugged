
###############################################################################
#
# UpdateItem
# Allows you to add or remove photos and tips from items on user-created lists.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateItem(Choreography):

    """
    Create a new instance of the UpdateItem Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Lists/UpdateItem')


    def new_input_set(self):
        return UpdateItemInputSet()

    def _make_result_set(self, result, path):
        return UpdateItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateItemChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateItem
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateItemInputSet(InputSet):
        """
        Set the value of the ItemID input for this choreography. ((required, string) The id of an item on a list that you wish to update.)
        """
        def set_ItemID(self, value):
            InputSet._set_input(self, 'ItemID', value)

        """
        Set the value of the ListID input for this choreography. ((required, string) The ID of a user-created list to update)
        """
        def set_ListID(self, value):
            InputSet._set_input(self, 'ListID', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The FourSquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the PhotoID input for this choreography. ((optional, string) If present and non-empty, adds a photo to this item. If present and empty, will remove the photo on this item. If the photo was a private checkin photo, it will be promoted to a public venue photo.)
        """
        def set_PhotoID(self, value):
            InputSet._set_input(self, 'PhotoID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Text input for this choreography. ((optional, string) If present, this creates a public tip on the venue and replaces any existing tip on the item. Cannot be used in conjuction with TipID or PhotoID.)
        """
        def set_Text(self, value):
            InputSet._set_input(self, 'Text', value)

        """
        Set the value of the TipID input for this choreography. ((optional, string) The id of a tip to add to the list. Cannot be used in conjunction with the Text and URL inputs. Note that one of the following must be specified: VenueID, TipID, ItemListID, or ItemID.)
        """
        def set_TipID(self, value):
            InputSet._set_input(self, 'TipID', value)

        """
        Set the value of the URL input for this choreography. ((optional, string) If adding a new tip using the Text input, this can associate a url with the tip.)
        """
        def set_URL(self, value):
            InputSet._set_input(self, 'URL', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateItem choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateItemResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateItemResultSet(response, path)
