Feature:A spotify user can create and amend playlists
  Scenario Outline: Creating and adding one song to a playlist
    Given that a playlist called Vikram's playlist is created in my spotify account
    When  I search for a track from album called <songs>
    And   I add my favourite track to my playlist
    Then  my favourite track is available in my playlist

    Examples:
    | songs |
    | Cheap Thrills |
    | Twinkle Twinkle Little Star |
    | Merry had a little lamb     |

